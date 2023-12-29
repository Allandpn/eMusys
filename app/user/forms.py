from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from app.models import Admin
from app import access_key



class RequestPassword(FlaskForm):
    email = StringField('Email', 
                       validators=[InputRequired(), Email()])
    submit = SubmitField('Enviar')
        
    def validate_email(self, email):
        email = Admin.query.filter_by(email = email.data).first()
        if email is None:
            raise ValidationError('Não existe conta com esse email. Verifique os dados e tente novamente')
        
        
        
class ResetPassword(FlaskForm):
    password = PasswordField('Password',
                            validators=[InputRequired(), Length(min=2)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Salvar')
    

    
class RegistrationForm(FlaskForm):
    usuario = StringField('Username',
                            validators=[InputRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                            validators=[InputRequired(), Email()])
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=2)])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[InputRequired(), EqualTo('password')])
    checksum = PasswordField('Chave de acesso',
                           validators=[InputRequired()])
    submit = SubmitField('Entrar')
    
    def validate_usuario(self, usuario):
        
        usuario_ = Admin.query.filter_by(usuario = usuario.data).first()
        if usuario_:
            raise ValidationError('Este usuário já existe. Escolha um nome de usuário diferente')
        
    def validate_email(self, email):
        email_ = Admin.query.filter_by(email = email.data).first()
        if email_:
            raise ValidationError('Este email já existe. Escolha um nome de email diferente')
        
    def validate_checksum(self, checksum): 
        if checksum.data != access_key:
            raise ValidationError('Chave de acesso inválida')
        
    

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=2)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
    
    

