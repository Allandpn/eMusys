from flask import render_template, request, url_for, redirect, flash, Blueprint
from flask_login import login_required
from app import db
from app.main.utils import perfil_admin
from app.admin.utils import get_unidade_brief, get_turma_brief, get_equipe_brief, get_unidade_selected, editUnidade, get_turma_selected, get_equipe_selected, create_unidade, create_turma, create_equipe, createTurma
from app.admin.forms import RegistroUnidade, RegistroTurma
from app.models import Turma, Unidade, Endereco, Coordenador, Instrumento


admin = Blueprint('admin', __name__)



@admin.route("/admin", methods=['GET', 'POST'])
@login_required
def admin_home():  
    unidades = get_unidade_brief()
    turmas = get_turma_brief()
    equipes = get_equipe_brief() 
    form_create_und, path_u = create_unidade()
    form_perfil, data_nasc, image_file = perfil_admin()
    form_create_turma, path_t = create_turma()
    form_create_equipe, path_e= create_equipe()    
    return render_template("admin.html", formPerfil=form_perfil, dataNasc=data_nasc, image_file=image_file, formCreateUnd=form_create_und, formCreateTurma=form_create_turma, formCreateEquipe=form_create_equipe, unidades = unidades, turmas = turmas, equipes = equipes, pane_u = path_u, pane_t = path_t, pane_e = path_e)



@admin.route("/admin/<path>", methods=['GET', 'POST'])
@login_required
def admin_path(path):   
    unidades = get_unidade_brief()
    turmas = get_turma_brief()
    equipes = get_equipe_brief() 
    form_create_und, pane = create_unidade()
    form_create_equipe, pane = create_equipe() 
    form_perfil, data_nasc, image_file = perfil_admin()
    form_create_turma, pane =  create_turma()
    return render_template("admin.html", formPerfil=form_perfil, dataNasc=data_nasc, image_file=image_file, formCreateUnd=form_create_und, formCreateTurma=form_create_turma, formCreateEquipe=form_create_equipe, unidades = unidades, turmas = turmas, equipes = equipes, pane = path)



@admin.route("/unidade/<id>/delete", methods=['POST'])
@login_required
def delete_unidade(id):  
    unidade = Unidade.query.get_or_404(id)
    db.session.delete(unidade)
    db.session.commit()
    flash('A unidade foi removida!', 'success')
    return redirect(url_for('admin.admin_path', path='unidade'))



@admin.route("/turma/<id>/delete", methods=['POST'])
@login_required
def delete_turma(id):  
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    flash('A turma foi removida!', 'success')
    return redirect(url_for('admin.admin_path', path='turma'))



@admin.route("/panel", methods=['GET'])
@login_required
def panel_select():         
    if request.args['pane'] == 'unidade':        
        panel = get_unidade_selected(request.args['id'])
    elif request.args['pane'] == 'turma':        
        panel = get_turma_selected(request.args['id'])
    elif request.args['pane'] == 'equipe':        
        panel = get_equipe_selected(request.args['id'])
    else:
        return redirect(url_for('admin.admin_home'))
    return panel



@admin.route("/unidade/<int:id>", methods=['GET', 'POST'])
def update_unidade(id):
    form = RegistroUnidade()
    form.gestor.choices = [(g.id, g.nome) for g in Coordenador.query.all()]
    if request.method == "POST" and request.form['type'] == 'formEditUnd':    
        if form.validate_on_submit():          
            editUnidade(form, id)            
            flash('Unidade atualizada com sucesso!', 'success')
            return redirect(url_for('admin.admin_path', path='unidade'))
        else:
            flash('Não foi possível atualizar os dados. Verifique as informações e tente novamente', 'danger')
    elif request.method == "GET":
        unidade = Unidade.query.filter_by(id = id).first()
        endereco = Endereco.query.filter_by(unidade_id = unidade.id).first()
        form.id.data = unidade.id  
        form.nome.data = unidade.nome
        form.endereco.data = endereco.rua
        form.bairro.data = endereco.bairro
        form.cidade.data = endereco.cidade
        form.cep.data = endereco.cep
        form.telefone.data = unidade.telefone
        form.email.data = unidade.email
        form.gestor.data = int(unidade.gestor)
          
    unidades = get_unidade_brief() 
    return render_template("admin.html", formEditUnd = form, unidades=unidades, pane = 'unidade')



@admin.route("/turma/<int:id>", methods=['GET', 'POST'])
def update_turma(id):
    form = RegistroTurma()
    form.unidade.choices = [(g.id, g.nome) for g in Unidade.query.all()]
    form.instrumento.choices = [(g.id, g.nome) for g in Instrumento.query.all()]
    form.nome_coordenador.choices = [(g.id, g.nome) for g in Coordenador.query.all()]
    path = 'turma'
    if request.method == "POST" and request.form['type'] == 'formCreateTurma':       
        if form.validate_on_submit():            
            createTurma(form)                       
            flash('Turma atualizada com sucesso!', 'success')  
            return redirect(url_for('admin.admin_path', path=path))
        else:
            flash('Não foi possível atualizar os dados. Verifique as informações e tente novamente', 'danger')
    elif request.method == "GET":
        turma = Turma.query.filter_by(id = id).first()
        form.id.data = turma.id  
        form.nome.data = turma.nome
        form.unidade.data = int(turma.unidade_id)
        form.instrumento.data = int(turma.instrumento_id)        
        form.dia_semana.data = int(turma.diaSemana)
        form.horario.data = turma.horario
        form.nome_coordenador.data = int(turma.coordenador_id)
          
    turmas = get_turma_brief() 
    return render_template("admin.html", formEditTurma = form, turmas=turmas, pane = path)