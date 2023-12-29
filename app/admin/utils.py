from PIL import Image
from flask import request, url_for, flash
from app import db
from app.models import Coordenador, Aluno, Instrumento, Turma, Unidade, Endereco, Tipoinstrumento
from app.main.utils import save_picture
from app.admin.forms import RegistroUnidade, RegistroTurma, RegistroEquipe
    
    
    
def create_unidade():    
    form = RegistroUnidade()
    form.gestor.choices = [(g.id, g.nome) for g in Coordenador.query.all()]
    path = 'unidade'
    if request.method == "POST" and request.form['type'] == 'formCreateUnd':        
        if form.validate_on_submit():            
            createUnidade(form)            
            flash('Unidade criada com sucesso!', 'success')
            return form, path
        else:
            flash('Não foi possível atualizar seus dados. Verifique as informações e tente novamente', 'danger')
    return form, path



def create_turma(): 
    form = RegistroTurma()
    form.unidade.choices = [(g.id, g.nome) for g in Unidade.query.all()]
    form.instrumento.choices = [(g.id, g.nome) for g in Tipoinstrumento.query.all()]
    form.nome_coordenador.choices = [(g.id, g.nome) for g in Coordenador.query.all()]
    path = 'turma'
    if request.method == "POST" and request.form['type'] == 'formCreateTurma':       
        if form.validate_on_submit():            
            createTurma(form)                       
            flash('Unidade criada com sucesso!', 'success')
            return form, path
        else:
            flash('Não foi possível atualizar seus dados. Verifique as informações e tente novamente', 'danger')
    return form, path



def create_equipe():        
    form = RegistroEquipe()
    form.unidade.choices = [(g.id, g.nome) for g in Unidade.query.all()]
    path = ''
    if request.method == "POST" and request.form['type'] == 'formCreateEquipe':     
        if form.validate_on_submit():            
            createEquipe(form)
            flash('Colaborador adicionado com sucesso!', 'success')
            return form, 'equipe' 
        else:
            flash('Não foi possível incluir o colaborador. Verifique as informações e tente novamente', 'danger')
    return form, path



def get_unidade_brief():
    unidades = Unidade.query.all()
    unidades_ = []    
    for unidade in unidades:
        unidade_ = {}
        unidade_["id"] = unidade.id 
        unidade_["nome"] = unidade.nome        
        unidade_["turma"] = Turma.query.filter_by(unidade_id = unidade.id).count()
        unidade_["aluno"] = Aluno.query.filter_by(unidade_id = unidade.id).count()
        unidade_["acervo"] = Instrumento.query.filter_by(unidade_id = unidade.id).count()
        unidade_["equipe"] = Coordenador.query.filter_by(unidade_id = unidade.id).count()
        unidades_.append(unidade_)
    return unidades_



def get_unidade_selected(id):
    unidade = Unidade.query.get(id)
    unidade_ = {}
    unidade_["id"] = unidade.id
    unidade_["url"] = url_for('admin.update_unidade', id=unidade.id)
    unidade_["nome"] = unidade.nome
    endereco = Endereco.query.filter_by(unidade_id = unidade.id).first()
    unidade_["endereco"] = (f'{endereco.rua}, {endereco.bairro}, {endereco.cidade}, {endereco.cep}')
    gestor = Coordenador.query.filter_by(id=unidade.gestor).first()
    unidade_["contato"] = (f'Gestor: {gestor.nome} Telefone: {unidade.telefone} Email: {unidade.email}') 
    unidade_["aluno"] = []
    for aluno in Aluno.query.filter_by(unidade_id = unidade.id).all():       
        unidade_["aluno"].append(aluno.nome)
       
    unidade_["equipe"] = []
    for equipe in Coordenador.query.filter_by(unidade_id = unidade.id).all():       
        unidade_["equipe"].append(equipe.nome)
       
    unidade_["curso"] = []
    for curso in Turma.query.filter_by(unidade_id = unidade.id).all():       
        unidade_["curso"].append(curso.nome)
       
    unidade_["acervo"] = []
    acervo = Instrumento.query.filter_by(unidade_id = unidade.id).with_entities(Instrumento.nome).distinct()
    for item in acervo:
        qnt = Instrumento.query.filter_by(unidade_id = unidade.id, nome = item.nome).count()
        nome = Tipoinstrumento.query.filter_by(id= item.nome).first()
        
        unidade_["acervo"].append(f'{nome.nome} - {str(qnt)}') 
        
    return unidade_



def get_turma_selected(id):
    turma = Turma.query.get(id)
    turma_ = {}
    turma_["id"] = turma.id
    turma_["url"] = url_for('admin.update_turma', id=turma.id)
    turma_["nome"] = turma.nome
    turma_["horario"] = (f'Horário: {str(turma.horario)[:5]}')
    coordenador = Coordenador.query.filter_by(id=turma.coordenador_id).first()    
    turma_["gestor"] = (f'Coordenador: {coordenador.nome}')
    turma_["aluno"] = []
    turma_["matricula"] = []
    for aluno in Aluno.query.filter_by(turma_id = turma.id).all():       
        turma_["aluno"].append(aluno.nome)
        data = aluno.dataAdmissao.strftime('%d-%m-%Y')
        turma_["matricula"].append(data)
      
    return turma_



def get_turma_brief():
    turmas = Turma.query.all()
    turmas_ = []    
    for turma in turmas:
        turma_ = {}        
        turma_["id"] = turma.id
        turma_["nome"] = turma.nome        
        turma_["unidade"] = turma.turma_unidade.nome
        turma_["dia_semana"] = turma.diaSemana
        turma_["horario"] = str(turma.horario)[:5]
        turma_["alunos"] = Aluno.query.filter_by(turma_id = turma.id).count()
        turmas_.append(turma_)
    return turmas_



def get_equipe_brief():
    equipes = Coordenador.query.all()
    equipes_ = []    
    for equipe in equipes:
        equipe_ = {}        
        equipe_["id"] = equipe.id
        equipe_["nome"] = equipe.nome        
        equipe_["funcao"] = equipe.funcao       
        equipe_["telefone"] = equipe.telefone
        equipe_["email"] = equipe.email        
        equipes_.append(equipe_)
    return equipes_



def get_equipe_selected(id):
    equipe = Coordenador.query.get(id)    
    equipe_ = {}       
    equipe_["nome"] = equipe.nome        
    equipe_["data_nascimento"] = equipe.dataNasc.strftime('%d-%m-%Y')
    endereco = Endereco.query.filter_by(coordenador_id=equipe.id).first()      
    equipe_["endereco"] = (f'{endereco.rua}, {endereco.bairro}, {endereco.cidade} , {endereco.cep}')
    equipe_["email"] = equipe.email
    equipe_["telefone"] = equipe.telefone
    return equipe_



def createUnidade(form):
    nome = form.nome.data
    gestor = form.gestor.data
    email = form.email.data
    telefone = form.telefone.data
    unidade = Unidade(nome = nome, gestor = gestor, email = email, telefone = telefone)
    db.session.add(unidade)
    db.session.commit()
    unidade_id = Unidade.query.filter_by(nome = form.nome.data).first()
    rua = form.endereco.data
    bairro = form.bairro.data
    cidade = form.cidade.data
    cep = form.cep.data
    endereco = Endereco(rua = rua, bairro = bairro, cidade = cidade, cep = cep, unidade_id = unidade_id.id)
    db.session.add(endereco)
    db.session.commit()



def editUnidade(form, id):
    unidade = Unidade.query.get(id)
    endereco = Endereco.query.filter_by(unidade_id = id).first()
    coordenador = Coordenador.query.filter_by(id = form.gestor.data).first()
    coordenador.unidade_id = id
    unidade.nome = form.nome.data
    unidade.gestor = form.gestor.data
    unidade.email = form.email.data
    unidade.telefone = form.telefone.data
    endereco.rua = form.endereco.data
    endereco.bairro = form.bairro.data
    endereco.cidade = form.cidade.data
    endereco.cep = form.cep.data
    db.session.commit()
    
    
    
def createTurma(form):
    nome = form.nome.data
    unidade =  form.unidade.data
    instrumento = form.instrumento.data
    dia_semana = form.dia_semana.data
    horario = form.horario.data
    coordenador_id = form.nome_coordenador.data
    turma = Turma(nome = nome, diaSemana = dia_semana, horario = horario, unidade_id = unidade, instrumento_id = instrumento,  coordenador_id = coordenador_id)
    db.session.add(turma)
    db.session.commit()
    
    

def createEquipe(form):
    nome = form.nome.data
    funcao = form.funcao.data
    email = form.email.data
    telefone = form.telefone.data    
    dataNasc = form.dataNasc.data
    unidade = form.unidade.data
    if not form.imagem.data :
        image_file = 'default.jpg'
    else:
        image_file = save_picture(form.imagem.data)
    equipe = Coordenador(nome = nome, funcao = funcao, email = email, telefone = telefone, dataNasc = dataNasc, image_file = image_file, unidade_id = unidade)
    db.session.add(equipe)
    db.session.commit()
    equipe_id = Coordenador.query.filter_by(email = form.email.data).first()
    rua = form.endereco.data
    bairro = form.bairro.data
    cidade = form.cidade.data
    cep = form.cep.data
    endereco = Endereco(rua = rua, bairro = bairro, cidade = cidade, cep = cep, coordenador_id = equipe_id.id)
    db.session.add(endereco)
    db.session.commit()