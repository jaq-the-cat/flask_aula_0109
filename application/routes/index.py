from flask import Blueprint
from application import app

bp = Blueprint('index', __name__)

@bp.get('/')
def index():
    return "Olá, Mundo!"

app.register_blueprint(bp)