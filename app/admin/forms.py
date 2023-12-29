from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DateField, SelectField, TimeField
from wtforms.validators import InputRequired, Length, Email, ValidationError
from app.models import Unidade, Turma, Coordenador

   

class RegistroUnidade(FlaskForm):
    id = StringField('id',
                              validators=[])
    nome = StringField('Nome da Unidade',
                              validators=[InputRequired(), Length(min=2,max=50)])
    gestor = SelectField('Nome do Coordenador', 
                                   coerce=int, validators=[InputRequired()])
    endereco = StringField('Endereço',
                              validators=[InputRequired(), Length(min=2,max=100)])
    bairro = StringField('Bairro',
                              validators=[InputRequired(), Length(min=2,max=20)])
    cidade = StringField('Cidade',
                              validators=[InputRequired(), Length(min=2,max=20)])
    cep = StringField('CEP',
                              validators=[InputRequired()])
    telefone = StringField('Telefone',
                              validators=[])
    email = StringField('Email',
                        validators=[Email()])
    type = StringField('RegistroUnidade')
    
    submit = SubmitField('Salvar')    
   
    
    def validate_nome(self, nome):            
        nome_set = Unidade.query.filter_by(id=self.id.data).first()
        if nome_set:
            if nome.data != nome_set.nome:
                nome_ = Unidade.query.filter_by(nome = nome.data).first()
                if nome_:
                    raise ValidationError('Este usuário já existe. Escolha um nome de usuário diferente')
        


class RegistroTurma(FlaskForm):
    id = StringField('id',
                              validators=[])
    nome = StringField('Nome da Turma',
                              validators=[InputRequired(), Length(min=2,max=50)])
    unidade = SelectField('Nome da Unidade', 
                          coerce=int, validators=[InputRequired()])
    instrumento = SelectField('Nome do Instrumento', 
                              coerce=int, validators=[InputRequired()])
    dia_semana = SelectField('Nome do Instrumento', 
                             choices=[(1,'Segunda'),(2,'Terça'),(3,'Quarta'),(4,'Quinta'),(5,'Sexta'),(6,'Sabado'),(7,'Domingo')], validators=[InputRequired()])
    horario = TimeField('Horario', 
                        validators=[InputRequired()])
    nome_coordenador = SelectField('Nome do Coordenador', 
                                   coerce=int)
    type = StringField('RegistroTurma')
    submit = SubmitField('Salvar')
    
    def validate_nome(self, nome):        
        if Turma.query.filter_by(nome = nome.data).first():
            raise ValidationError('Este nome já existe. Escolha um nome diferente para a turma')
        
        
class RegistroEquipe(FlaskForm):
    id = StringField('id',
                              validators=[])
    imagem = FileField("Imagem", 
                      validators=[FileAllowed(['jpg', 'png'])])
    nome = StringField('Nome',
                              validators=[InputRequired(), Length(min=2,max=50)])
    funcao = StringField('Nome',
                              validators=[InputRequired(), Length(min=2,max=50)])
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    telefone = StringField('Telefone',
                              validators=[])
    dataNasc = DateField('Data de Nascimento', format="%Y-%m-%d", validators=[])
    endereco = StringField('Endereço',
                              validators=[InputRequired(), Length(min=2,max=100)])
    bairro = StringField('Bairro',
                              validators=[InputRequired(), Length(min=2,max=20)])
    cidade = StringField('Cidade',
                              validators=[InputRequired(), Length(min=2,max=20)])
    cep = StringField('CEP',
                              validators=[InputRequired()])
    unidade = SelectField('Unidade', 
                                   coerce=int, validators=[])
    type = StringField('RegistroEquipe')
    submit = SubmitField('Salvar')
    
    def validate_nome(self, nome):        
        if Coordenador.query.filter_by(nome = nome.data).first():
            raise ValidationError('Este nome já existe. Escolha um nome diferente para o colaborador')
    
    def validate_email(self, email):        
        if Coordenador.query.filter_by(email = email.data).first():
            raise ValidationError('Este email já existe. Escolha um email diferente para o colaborador')
        
    def validate_telefone(self, telefone):        
        if Coordenador.query.filter_by(telefone = telefone.data).first():
            raise ValidationError('Este telefone já existe. Escolha um telefone diferente para o colaborador')
        