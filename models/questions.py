from app import db, app


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pergunta = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, dados):
        self.pergunta = dados['pergunta']

with app.app_context():
    db.create_all()

