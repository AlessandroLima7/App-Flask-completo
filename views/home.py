from flask import render_template, Blueprint, redirect, request
from models.questions import Questions
from processors import cadastro, consultas, deletes

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home')
def home():
    return render_template('home.html', titulo='Home', dados=Questions.query.all())

@home_bp.route('/cadastro')
def realiza_cadastro():
    return render_template('cadastrar.html', titulo="Cadastro")

@home_bp.route('/api', methods=['POST'])
def consulta():
    return consultas.realizar_consulta(request) 

@home_bp.route('/api', methods=['DELETE'])
def delete():
    return deletes.deletar(request)

@home_bp.route('/api/cadastrar', methods=['POST'])
def cadastrar():
    print(request.json)
    return cadastro.cadastrar(request)


