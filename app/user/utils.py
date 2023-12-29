import os
from flask import url_for, current_app
from flask_login import current_user
from app import db, bcrypt, mail
from app.main.utils import save_picture
from app.models import Admin
from flask_mail import Message



def createUser(form):
    usuario = form.usuario.data
    email = form.email.data
    senha = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    admin = Admin(usuario = usuario, email = email, checksum = senha)
    db.session.add(admin)
    db.session.commit() 
    

def updateUser(form):
    current_user.usuario = form.usuario.data
    current_user.nome = form.nome.data
    current_user.email = form.email.data
    current_user.telefone = form.telefone.data
    if form.dataNasc.data:
        current_user.dataNasc = form.dataNasc.data
    if form.imagem.data :
        if current_user.image_file != 'default.jpg':
            try:
                picture_path = os.path.join(current_app.root_path, 'static\image_profiles', current_user.image_file)
                os.remove(picture_path)
            except:
                pass  
        picture_file = save_picture(form.imagem.data)
        current_user.image_file = picture_file    
    if form.password.data:        
        current_user.checksum = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    db.session.commit()



def send_request_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                  sender='allandpncursos@gmail.com', 
                  recipients=[user.email])
    msg.body = f'''Para recuperar sua senha, acesse o link abaixo:
    {url_for('reset_password', token=token, _external=True)}
    
    Se você não fez essa solicitação igonre esse mail e nenhuma alteraão será efetuada
    '''
    mail.send(msg)
    