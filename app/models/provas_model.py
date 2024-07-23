from app.models.base_model import BaseModel
from app.models.questoes_model import Questoes
from app.extensions import db

class Provas(BaseModel):
    __tablename__ = 'provas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(500), default='')
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=True)
    professor = db.relationship('Professores', back_populates='provas', foreign_keys=[professor_id], viewonly=True)
    questoes = db.relationship('Questoes', secondary='provas_questoes', back_populates='provas')

    def __repr__(self):
        return self.descricao