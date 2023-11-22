from models.questions import Questions

def realizar_consulta(req):
    dados = req.json
    if(dados['id'] != ''):
        dados = Questions.query.filter_by(id=int(dados['id']))
    else:
        dados = Questions.query.all()
    dto = []
    for i in dados:
        registro = {"id": f"{i.id}","pergunta": f"{i.pergunta}"}
        dto.append(registro)
    return dto
        
