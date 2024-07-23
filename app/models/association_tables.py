from app.extensions import db

provas_questoes = db.Table(
    'provas_questoes',
    db.Column('prova_id', db.Integer, db.ForeignKey('provas.id', name='fk_provas_id')),
    db.Column('questao_id', db.Integer, db.ForeignKey('questoes.id', name='fk_questoes_id'))
)