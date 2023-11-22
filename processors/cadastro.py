from app import db
from models.questions import Questions

def cadastrar(dados):
    db.session.add(Questions(dados))
    db.session.commit()