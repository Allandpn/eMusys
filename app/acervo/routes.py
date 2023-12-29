from flask import Blueprint, render_template
from flask_login import login_required
from app.acervo.utils import get_instrumento_brief, create_tipo_instrumento, create_instrumento
from app.main.utils import perfil_admin

acervo = Blueprint('acervo', __name__)


@acervo.route("/acervo", methods=['GET', 'POST'])
@login_required
def acervo_home():
    instrumentos = get_instrumento_brief()  
    formCreateTipoInstrumento = create_tipo_instrumento()
    formCreateInstrumento = create_instrumento()
    formPerfil, dataNasc, image_file = perfil_admin()
    return render_template("acervo.html", formPerfil=formPerfil, dataNasc=dataNasc, image_file=image_file, formCreateTipoInstrumento=formCreateTipoInstrumento, formCreateInstrumento=formCreateInstrumento, instrumentos=instrumentos)