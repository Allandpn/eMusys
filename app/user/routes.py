from flask import Blueprint, render_template
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, current_user, logout_user
from app import db, bcrypt
from app.user.utils import createUser, send_request_email
from app.user.forms import RegistrationForm, LoginForm, RequestPassword, ResetPassword
from app.models import Admin

user = Blueprint('user', __name__)



@user.route("/register", methods=['GET', 'POST'] )
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.logout'))
    form = RegistrationForm()
    if request.method == "POST":   
        if  form.validate_on_submit():
            createUser(form)
            flash('Sua conta foi criada com sucesso!', 'success')
            return redirect(url_for('user.login'))
        else:
            flash('Não foi possível criar sua conta. Confirme seus dados e tente novamente', 'danger')
    return render_template("register.html", title= 'Register', form=form)




@user.route("/", methods=['GET', 'POST'] )
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.logout'))
    form = LoginForm()
    if request.method == "POST":        
        if form.validate_on_submit():
            usuario = Admin.query.filter_by(email=form.email.data).first()
            if usuario and bcrypt.check_password_hash(usuario.checksum, form.password.data):
                login_user(usuario, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
            else:
                flash('Não foi possível acessar sua conta. Confirme seus dados e tente novamente', 'danger')
    return render_template("login.html", title='Login', form=form)



@user.route("/logout", methods=['GET', 'POST'] )
def logout():
    logout_user()
    return redirect(url_for('user.login'))
    


@user.route("/reset_password", methods=["GET", "POST"])
def request_password():
    if current_user.is_authenticated:
        return redirect(url_for('user.logout'))
    form = RequestPassword()
    if form.validate_on_submit():
        user = Admin.query.filter_by(email = form.email.data).first()
        send_request_email(user)
        flash('Foi enviado um email com as instruções para recuperar sua senha', 'info')
        return redirect(url_for('user.login'))
    return render_template('request_password.html', title="Recuperar Senha", form=form)



@user.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('user.logout'))
    user = Admin.verify_reset_token(token)
    if not user:
        flash('O link para recuperar a senha expirou. Envie o link novamente', 'warning')
        return redirect(url_for('user.request_password'))
    form = ResetPassword()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.checksum = hash_password
        db.session.commit()
        flash('Sua senha foi atualizada com sucesso', 'success')
        return redirect(url_for('user.login'))
    return render_template('reset_password.html', title="Atualizar Senha", form=form)