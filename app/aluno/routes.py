from flask import Blueprint, render_template, request
from flask_login import login_required
from app.aluno.utils import create_aluno, get_alunos_brief, get_alunos_select
from app.main.utils import perfil_admin
from app.models import Aluno

aluno = Blueprint('aluno', __name__)


@aluno.route("/alunos", methods=['GET', 'POST'])
@login_required
def alunos():
    form_create_aluno = create_aluno()
    alunos = get_alunos_brief()  
    form_perfil, data_nasc, image_file = perfil_admin()
    return render_template("alunos.html", formPerfil=form_perfil, dataNasc=data_nasc, image_file=image_file, alunos = alunos, formCreateAluno = form_create_aluno)


@aluno.route("/alunos/<int:id>", methods=['GET', 'POST'])
@login_required
def alunos_select(id):
    aluno = get_alunos_select(id) 
    return aluno



@aluno.route("/aluno/cadastro/<int:id>", methods=['GET', 'POST'])
@login_required
def alunos_edit(id):
    form_edit_aluno = create_aluno()
    alunos = get_alunos_brief()
    aluno = get_alunos_select(id)   
    form_perfil, data_nasc, image_file = perfil_admin()
    if request.method == "GET":
        aluno = Aluno.query.get(id)
        form_edit_aluno.nome.data = aluno.nome
        form_edit_aluno.email.data = aluno.email
        form_edit_aluno.telefone.data = aluno.telefone
        form_edit_aluno.data_nasc.data = aluno.dataNasc
        form_edit_aluno.data_admissao.data = aluno.dataAdmissao
        form_edit_aluno.data_desligamento.data = aluno.dataDesligamento
        form_edit_aluno.nome_responsavel.data = aluno.nomeResponsavel
        form_edit_aluno.email_responsavel.data = aluno.emailResponsavel
        form_edit_aluno.telefone_responsavel.data = aluno.telefoneResponsavel
        form_edit_aluno.anotacoes.data = aluno.anotacoesAluno
    return render_template("alunos.html", formPerfil=form_perfil, dataNasc=data_nasc, image_file=image_file, alunos = alunos, formEditAluno = form_edit_aluno, aluno = aluno)