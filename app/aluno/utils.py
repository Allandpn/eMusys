from flask import request, flash, current_app
from app import db
from app.aluno.forms import RegistroAluno
from app.models import Aluno, Instrumento, Turma, Endereco, Tipoinstrumento
from app.main.utils import save_picture

def create_aluno():
    form = RegistroAluno()
    form.turma.choices = [(g.id, g.nome) for g in Turma.query.all()]
    if request.method == "POST" and request.form['type'] == 'formCreateAluno':
        if form.validate_on_submit():            
            createAluno(form)         
            flash('Aluno adicionado com sucesso!', 'success')
        else:
            flash('Não foi possível incluir o aluno. Verifique as informações e tente novamente', 'danger')
    return form



def createAluno(form):
    nome = form.nome.data
    email = form.email.data
    telefone = form.telefone.data    
    data_nasc = form.data_nasc.data
    data_admissao = form.data_admissao.data
    data_desligamento = form.data_desligamento.data
    nome_responsavel = form.nome_responsavel.data
    email_responsavel = form.email_responsavel.data
    telefone_responsavel = form.telefone_responsavel.data
    anotacoes = form.anotacoes.data   
     
    if not form.imagem.data :
        image_file = 'default.jpg'
    else:
        image_file = save_picture(form.imagem.data)
        
    if form.turma.data:    
        turma = form.turma.data
        unidade = Turma.query.filter_by(id = turma).first()
        unidade_id = unidade.unidade_id
    else:
        turma = None
         
    aluno = Aluno(nome = nome, email = email, telefone = telefone, dataNasc = data_nasc, dataAdmissao = data_admissao, dataDesligamento = data_desligamento, nomeResponsavel = nome_responsavel, emailResponsavel = email_responsavel, telefoneResponsavel = telefone_responsavel, anotacoesAluno = anotacoes, turma_id = turma, image_file = image_file, unidade_id = unidade_id)
    db.session.add(aluno)
    db.session.commit()
    aluno_id = Aluno.query.filter_by(email = form.email.data).first()
    rua = form.endereco.data
    bairro = form.bairro.data
    cidade = form.cidade.data
    cep = form.cep.data
    endereco = Endereco(rua = rua, bairro = bairro, cidade = cidade, cep = cep, aluno_id = aluno_id.id)
    db.session.add(endereco)
    db.session.commit()
    
    
    
def get_alunos_brief():
    alunos = Aluno.query.all()
    alunos_ = []    
    for aluno in alunos:
        aluno_ = {}
        aluno_["id"] = aluno.id
        aluno_["nome"] = aluno.nome
        aluno_["data_nascimento"] = aluno.dataNasc
        if aluno.aluno_turma:                     
            aluno_["turma"] = aluno.aluno_turma.nome
            aluno_["unidade"] = aluno.aluno_unidade.nome
            instrumento = Tipoinstrumento.query.filter_by(id = aluno.aluno_turma.instrumento_id).first()
            aluno_["instrumento"] = instrumento.nome
        else:
            aluno_["instrumento"] = "-"
            aluno_["turma"] = "-"
            aluno_["unidade"] = "-"
        aluno_["data_admissao"] = aluno.dataAdmissao.strftime("%m/%d/%Y")        
        alunos_.append(aluno_)
    return alunos_



def get_alunos_select(id):
    aluno = Aluno.query.get(id)
    aluno_ = {}
    aluno_["id"] = aluno.id
    aluno_["nome"] = aluno.nome
    aluno_["data_nascimento"] = aluno.dataNasc.strftime('%d-%m-%Y')
    endereco = Endereco.query.filter_by(aluno_id = aluno.id).first()
    aluno_["endereco"] = (f'{endereco.rua}, {endereco.bairro}, {endereco.cidade}, {endereco.cep}')
    aluno_["email"] = aluno.email
    aluno_["telefone"] = aluno.telefone
    aluno_["nome_resp"] = aluno.nomeResponsavel
    aluno_["telefone_resp"] = aluno.telefoneResponsavel
    aluno_["email_resp"] = aluno.emailResponsavel
    if aluno.aluno_turma:                     
        aluno_["turma"] = aluno.aluno_turma.nome
        aluno_["unidade"] = aluno.aluno_unidade.nome
        instrumento = Tipoinstrumento.query.filter_by(id = aluno.aluno_turma.instrumento_id).first()
        current_app.logger.info(instrumento.nome)
        aluno_["instrumento"] = instrumento.nome
    else:
        aluno_["instrumento"] = "-"
        aluno_["turma"] = "-"
        aluno_["unidade"] = "-"
    aluno_["data_admissao"] = aluno.dataAdmissao.strftime('%d-%m-%Y')    
    aluno_["anotacoes"] = aluno.anotacoesAluno
    if aluno.dataDesligamento:
        aluno_["data_desligamento"] = aluno.dataDesligamento.strftime('%d-%m-%Y')
    else:
        aluno_["data_desligamento"] = ""  
    return aluno_
