from flask import render_template, Blueprint, redirect, request
from models.questions import Questions
from processors import cadastro, consultas

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html', titulo='Home', dados=Questions.query.all())

@home_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    cadastro.cadastrar({'pergunta':request.form['pergunta']})
    return redirect('home')

@home_bp.route('/cadastro')
def realiza_cadastro():
    return render_template('cadastrar.html', titulo="Cadastro")

@home_bp.route('/api', methods=['POST'])
def teste_api():
    return consultas.realizar_consulta(request) 

