from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(usuario_id):
    return Admin.query.get(int(usuario_id))


class Admin(db.Model, UserMixin):    
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    nome = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=True)
    dataNasc = db.Column(db.DateTime, unique=False, nullable=True)    
    checksum = db.Column(db.String(100), unique=False, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    
    def get_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'admin_id': self.id})
    
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            admin_id = s.loads(token)['admin_id']
        except:
            return None
        return Admin.query.get(admin_id) 
    
    
    def __rep__(self):
        return f'nome: {self.nome}, id: {self.id}'
    
    
class Coordenador(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=False, nullable=False)
    funcao = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=True)
    dataNasc = db.Column(db.DateTime, unique=False, nullable=True)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=True)
    turmas = db.relationship('Turma', backref='turmas_coord', lazy=True, cascade="all, delete")    
    endereco = db.relationship('Endereco', backref='endereco_coord', lazy=True, cascade="all, delete")
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    telefone = db.Column(db.String(20), unique=False, nullable=True)
    dataNasc = db.Column(db.DateTime, unique=False, nullable=True)
    dataAdmissao = db.Column(db.DateTime, unique=False, nullable=True)
    dataDesligamento = db.Column(db.DateTime, unique=False, nullable=True)    
    nomeResponsavel = db.Column(db.String(50), unique=False, nullable=True)    
    telefoneResponsavel = db.Column(db.String(20), unique=False, nullable=True)      
    emailResponsavel = db.Column(db.String(100), unique=False, nullable=True)      
    anotacoesAluno = db.Column(db.String(400), unique=False, nullable=True)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=True)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=True)
    emprestimos = db.relationship('Emprestimo', backref='emprestimo_aluno', lazy=True, cascade="all, delete") 
    contribuicoes = db.relationship('Contribuicao', backref='contribuicao_aluno', lazy=True, cascade="all, delete")    
    enderecos = db.relationship('Endereco', backref='endereco_aluno', lazy=True, cascade="all, delete")
    historico_aluno = db.relationship('HistoricoAluno', backref='historico_aluno', lazy=True, cascade="all, delete")
    matricula_aluno = db.relationship('Matricula', backref='matricula_aluno', lazy=True, cascade="all, delete")
    
class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    
class HistoricoAluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    dataAdmissao = db.Column(db.DateTime, unique=False, nullable=True)
    dataDesligamento = db.Column(db.DateTime, unique=False, nullable=True)
    

class Tipoinstrumento(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=False, nullable=False)
    codigo = db.Column(db.String(5), unique=False, nullable=False)    
    instrumentos = db.relationship('Instrumento', backref='instrumento_tipo', lazy=True, cascade="all, delete")
  
    
class Instrumento(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer, db.ForeignKey('tipoinstrumento.id'), nullable=False)
    etiqueta = db.Column(db.String(5), unique=True, nullable=False)
    marca = db.Column(db.String(50), unique=False, nullable=True)
    dataAquisicao = db.Column(db.DateTime, unique=False, nullable=True)
    anotacao = db.Column(db.String(300), unique=False, nullable=True)
    estado_instrumento = db.Column(db.String(50), unique=False, nullable=True)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=False)
    emprestimos = db.relationship('Emprestimo', backref='emprestimo_instrumento', lazy=True, cascade="all, delete")
    turmas = db.relationship('Turma', backref='turma_instrumento', lazy=True, cascade="all, delete")  
    
class Turma(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=False, nullable=False)    
    diaSemana = db.Column(db.String(20), unique=False, nullable=False)
    horario = db.Column(db.Time, unique=False, nullable=True)
    instrumento_id = db.Column(db.Integer, db.ForeignKey('instrumento.id'), nullable=False)   
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=False)    
    coordenador_id = db.Column(db.Integer, db.ForeignKey('coordenador.id'), nullable=True)
    historico_turma = db.relationship('HistoricoAluno', backref='historico_turma', lazy=True, cascade="all, delete")      
    alunos = db.relationship('Aluno', backref='aluno_turma', lazy=True, cascade="all, delete")        
    
class Unidade(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    gestor = db.Column(db.Integer, unique=False, nullable=True)
    email = db.Column(db.String(100), unique=False, nullable=True)
    telefone = db.Column(db.String(20), unique=False, nullable=True)
    instrumentos = db.relationship('Instrumento', backref='instrumento_unidade', lazy=True)
    turmas = db.relationship('Turma', backref='turma_unidade', lazy=True, cascade="all, delete")
    endereco = db.relationship('Endereco', backref='endereco_unidade', lazy=True)
    alunos = db.relationship('Aluno', backref='aluno_unidade', lazy=True )    
    equipe = db.relationship('Coordenador', backref='coord_unidade', lazy=True) 
    
class Emprestimo(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    dataRetirada = db.Column(db.DateTime, unique=False, nullable=True, default=datetime.utcnow)
    dataDevolucao = db.Column(db.DateTime, unique=False, nullable=True)       
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    instrumento_id = db.Column(db.Integer, db.ForeignKey('instrumento.id'), nullable=False)   
    
class Contribuicao(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, unique=False, nullable=False)
    dataContribuicao = db.Column(db.DateTime, unique=False, nullable=True, default=datetime.utcnow)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(100), unique=False, nullable=True)
    numero = db.Column(db.Integer, unique=False, nullable=True)
    bairro = db.Column(db.String(50), unique=False, nullable=True)   
    complemento = db.Column(db.String(50), unique=False, nullable=True) 
    cidade = db.Column(db.String(50), unique=False, nullable=True)
    cep = db.Column(db.String(12), unique=False, nullable=True)  
    estado = db.Column(db.String(50), unique=False, nullable=True)    
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'), nullable=True)
    coordenador_id = db.Column(db.Integer, db.ForeignKey('coordenador.id'), nullable=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=True) 