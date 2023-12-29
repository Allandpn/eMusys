import os
import secrets
from PIL import Image
from app import db
from flask import request, url_for, flash, current_app
from flask_login import current_user
from app.main.forms import PerfilForm



def perfil_admin():
    form = PerfilForm()
    data_nasc = str(current_user.dataNasc)[:10]    
    if request.method == "POST" and request.form['type'] == 'formPerfil':
        if form.validate_on_submit():            
            updateUser(form)            
            flash('Sua dados foram atualizados!', 'success')
        else:
            flash('Não foi possível atualizar seus dados. Verifique as informações e tente novamente', 'danger')
    image_file = url_for('static', filename='image_profiles/' + current_user.image_file)
    return form, data_nasc, image_file


# Configura imagem de perfil
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static\image_profiles', picture_fn)   
     
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)  
      
    return picture_fn



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