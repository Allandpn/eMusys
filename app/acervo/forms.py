from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError, Optional
from app.models import  Tipoinstrumento



class RegistroTipoInstrumento(FlaskForm):
    instrumento = StringField('Marca',
                              validators=[InputRequired(), Length(min=2,max=50)])
    codigo = StringField('Marca',
                              validators=[InputRequired(), Length(min=2,max=4)])
    type = StringField('RegistroTipoInstrumento')
    submit = SubmitField('Salvar')
    
    def validate_instrumento(self, instrumento):        
        if Tipoinstrumento.query.filter_by(nome = instrumento.data).first():
            raise ValidationError('Este instrumento já existe. Escolha um nome de instrumento diferente')
        
    def validate_codigo(self, codigo):        
        if Tipoinstrumento.query.filter_by(codigo = codigo.data).first():
            raise ValidationError('Este codigo já existe. Escolha um codigo diferente')
   
   
   

class RegistroInstrumento(FlaskForm):
    instrumento = SelectField('Instrumento', 
                                   coerce=int, validators=[])
    marca = StringField('Marca',
                              validators=[InputRequired(), Length(min=2,max=50)])
    estado_instrumento = SelectField('Turma', 
                                   choices=[(1, 'Novo'),(2, 'Muito bom'),(3, 'Bom'),(4, 'Regular'),(5, 'Ruim')], validators=[Optional()])
    unidade = SelectField('Unidade', 
                                   coerce=int, validators=[])
    data_aquisicao = DateField('Data de Aquisição', format="%Y-%m-%d", validators=[Optional()])
    anotacoes = TextAreaField('Anotações',
                              validators=[Length(max=300)])
    type = StringField('RegistroInstrumento')
    submit = SubmitField('Salvar')