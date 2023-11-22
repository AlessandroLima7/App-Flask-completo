from models.questions import Questions

def realizar_consulta(req):
    id = req.json
    if(id['id'] != ''):
        dados = Questions.query.filter_by(id=id['id'])
    else:
        dados = Questions.query.all()
    dto = []
    for i in dados:
        registro = {"id": f"{i.id}","pergunta": f"{i.pergunta}"}
        dto.append(registro)
    return dto
        
