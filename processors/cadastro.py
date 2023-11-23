from app import db
from models.questions import Questions

def cadastrar(req):
    dados = req.json
    db.session.add(Questions(dados))
    db.session.commit()

    return {"msg": "Cadastrado com sucesso."}