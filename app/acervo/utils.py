from flask import request, flash
from app import db
from app.acervo.forms import RegistroInstrumento, RegistroTipoInstrumento
from app.models import Instrumento, Unidade, Emprestimo, Tipoinstrumento



def create_tipo_instrumento():
    form = RegistroTipoInstrumento()
    if request.method == "POST" and request.form['type'] == 'formCreateTipoInstrumento':
        if form.validate_on_submit():
            createTipoInstrumento(form)       
            flash('Instrumento adicionado com sucesso!', 'success')
        else:
            flash('Não foi possível incluir o instrumento. Verifique as informações e tente novamente', 'danger')
    return form


def create_instrumento():
    form = RegistroInstrumento()
    form.instrumento.choices = [(g.id, g.nome) for g in Tipoinstrumento.query.all()]
    form.unidade.choices = [(g.id, g.nome) for g in Unidade.query.all()]
    if request.method == "POST" and request.form['type'] == 'formCreateInstrumento':
            
        if form.validate_on_submit():
            etiqueta = createInstrumento(form)
                  
            flash(f'Instrumento adicionado com sucesso! A etiqueta é : {etiqueta}', 'success')
        else:
            flash('Não foi possível incluir o instrumento. Verifique as informações e tente novamente', 'danger')
    return form


def get_instrumento_brief():
    instrumentos = Instrumento.query.all()
    instrumentos_ = []    
    for instrumento in instrumentos:
        
        instrumento_ = {}
        instrumento_["cod"] = instrumento.etiqueta       
        instrumento_["nome"] = instrumento.instrumento_tipo.nome
        instrumento_["marca"] = instrumento.marca        
        instrumento_["unidade"] = instrumento.instrumento_unidade.nome
        emprestimo = Emprestimo.query.filter_by(instrumento_id = instrumento.id).first()
        if emprestimo: 
            instrumento_["emprestimo"] = emprestimo.dataRetirada
            instrumento_["aluno"] = emprestimo.emprestimo_aluno.nome
        else:
            instrumento_["emprestimo"] = '-'
            instrumento_["aluno"] = '-' 
        instrumentos_.append(instrumento_)
    return instrumentos_


def createTipoInstrumento(form):
    nome = form.instrumento.data
    codigo = form.codigo.data
    tipo_instrumento = Tipoinstrumento(nome = nome, codigo = codigo)
    db.session.add(tipo_instrumento)
    db.session.commit()   
    
    
    
def createInstrumento(form):
    nome = form.instrumento.data
    marca = form.marca.data
    data_aquisicao = form.data_aquisicao.data
    estado_instrumento = form.estado_instrumento.data
    unidade = Unidade.query.filter_by(id = form.unidade.data).first()    
    etiqueta = 'etq'
    anotacao = form.anotacoes.data
    instrumento = Instrumento(nome = nome, marca = marca, estado_instrumento = estado_instrumento, unidade_id = unidade.id, etiqueta = etiqueta, anotacao = anotacao, dataAquisicao = data_aquisicao)
    
    db.session.add(instrumento)
    
    db.session.flush()
    
    cod =  Tipoinstrumento.query.filter_by(id = form.instrumento.data).first()
    count =  Instrumento.query.filter_by(nome = form.instrumento.data).count()
    instrumento.etiqueta = cod.codigo + str(count)
    db.session.commit()
    return instrumento.etiqueta