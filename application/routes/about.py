from flask import Blueprint
from application import app
import os

bp = Blueprint('about', __name__, url_prefix='/sobre')

@bp.get('/')
def index():
    nome = os.getenv("NOME", "Mundo")
    return f"Olá, {nome}!"

app.register_blueprint(bp)