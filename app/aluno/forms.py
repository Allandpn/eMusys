from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, Email, ValidationError, Optional
from app.models import Aluno


class RegistroAluno(FlaskForm):
    imagem = FileField("Imagem", 
                      validators=[FileAllowed(['jpg', 'png'])])
    nome = StringField('Nome',
                              validators=[InputRequired(), Length(min=2,max=20)])
    turma = SelectField('Turma', 
                                   coerce=int, validators=[Optional()])
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    telefone = StringField('Telefone',
                              validators=[])
    data_nasc = DateField('Data de Nascimento', format="%Y-%m-%d", validators=[])
    data_admissao = DateField('Data de Admissão', format="%Y-%m-%d", validators=[Optional()])
    data_desligamento = DateField('Data de Desligamento', format="%Y-%m-%d", validators=[])
    nome_responsavel = StringField('Nome',
                              validators=[Length(min=2,max=20)])
    email_responsavel = StringField('Email',
                        validators=[Email()])
    telefone_responsavel = StringField('Telefone',
                              validators=[])
    anotacoes = TextAreaField('Anotações',
                              validators=[Length(max=400)])
    endereco = StringField('Endereço',
                              validators=[Length(min=2,max=100)])
    bairro = StringField('Bairro',
                              validators=[Length(min=2,max=20)])
    cidade = StringField('Cidade',
                              validators=[Length(min=2,max=20)])
    cep = StringField('CEP',
                              validators=[])
        
    type = StringField('RegistroAluno')
    submit = SubmitField('Salvar')
    
    def validate_email(self, email):        
        if Aluno.query.filter_by(email = email.data).first():
            raise ValidationError('Este email já existe. Escolha um email diferente para o colaborador')