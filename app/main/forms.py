from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import Length, Email, EqualTo, ValidationError, Optional
from app.models import Admin


class PerfilForm(FlaskForm):    
    imagem = FileField("Imagem de Perfil", validators=[FileAllowed(['jpg', 'png'])])   
    usuario = StringField('Usuario',
                              validators=[Length(min=2,max=20)])
    nome = StringField('Nome',
                              validators=[Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[Email()])
    telefone = StringField('Telefone',
                              validators=[])
    dataNasc = DateField('Data de Nascimento', format="%Y-%m-%d", validators=[Optional()])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password',
                                    validators=[EqualTo('password')])
    type = StringField('PerfilForm')
    submit = SubmitField('Salvar')
    
    def validate_usuario(self, usuario):
        if usuario.data != current_user.usuario:
            usuario_ = Admin.query.filter_by(usuario = usuario.data).first()
            if usuario_:
                raise ValidationError('Este usuário já existe. Escolha um nome de usuário diferente')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email_ = Admin.query.filter_by(email = email.data).first()
            if email_:
                raise ValidationError('Este email já existe. Escolha um nome de email diferente')
            
    def validate_password(self, password):
        if password.data and len(password.data) < 3:
            raise ValidationError('A senha deve possui pelo menos 03 caracteres')