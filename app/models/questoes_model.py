from app.models.base_model import BaseModel
from app.extensions import db

class Questoes(BaseModel):
    __tablename__ = 'questoes'
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.String(500), default='')
    resposta = db.Column(db.String(500), default='')
    provas = db.relationship('Provas', secondary='provas_questoes', back_populates='questoes')

    def __repr__(self):
        return self.pergunta