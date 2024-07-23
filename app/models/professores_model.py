from app.models.base_model import BaseModel
from app.models.provas_model import Provas
from app.extensions import db

class Professores(BaseModel):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    provas = db.relationship('Provas', back_populates='professor', lazy=True)