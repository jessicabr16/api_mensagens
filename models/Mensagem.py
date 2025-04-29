from utils import db

class Mensagem(db.Model):
    __tablename__="mensagem"
    id = db.Column(db.Integer, primary_key = True)
    conteudo = db.Column(db.String(100))

    def __init__(self, conteudo):
        self.conteudo = conteudo


    def __repr__(self):
        return "Mensagem {}>".format(self.conteudo)