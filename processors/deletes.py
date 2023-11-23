from models.questions import Questions
from app import db

def deletar(req):
    dados = req.json
    if(dados['lista_ids'] is None):
        return {"msg": "Nenhum item selecionado para exclusão."}
    for i in dados['lista_ids']:
        item = Questions.query.filter_by(id=int(i)).first()
        db.session.delete(item)
        db.session.commit()    
    return {"msg": "Excluído com sucesso."}