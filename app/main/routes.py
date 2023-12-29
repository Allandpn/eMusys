from flask import Blueprint, render_template
from flask_login import login_required
from app.main.utils import perfil_admin

main = Blueprint('main', __name__)



@main.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():    
    form_perfil, data_nasc, image_file = perfil_admin()
    return render_template("dashboard.html", formPerfil=form_perfil, dataNasc=data_nasc, image_file=image_file)
