from flask import request
from flask.views import MethodView

from app.models.provas_model import Provas
from app.models.professores_model import Professores
from app.models.questoes_model import Questoes
from app.schemas.provas_schema import ProvasSchema

class ProvasList(MethodView):
    def post(self):
        data = request.get_json(force=True)
        schema = ProvasSchema()

        professor_id = data.get('professor_id', None)
        questoes_ids = data.pop('questoes_ids', [])

        prova = schema.load(data)
        
        if questoes_ids:
            questoes = Questoes.query.filter(Questoes.id.in_(questoes_ids)).all()
            prova.questoes = questoes

        prova.save()

        return schema.dump(prova), 201

    def get(self):
        provas = Provas.query.all()
        schema = ProvasSchema(many=True)
        return schema.dump(provas)
    
class ProvasDetail(MethodView):
    def get(self, prova_id):
        prova = Provas.query.filter_by(id=prova_id).first_or_404()
        schema = ProvasSchema()
        return schema.dump(prova), 200
    
    def delete(self, prova_id):
        prova = Provas.query.filter_by(id=prova_id).first_or_404()
        prova.delete(prova)
        return {}, 204

    def patch(self, prova_id):
        data = request.get_json(force=True)
        schema = ProvasSchema(partial=True)
        prova = Provas.query.filter_by(id=prova_id).first_or_404()

        professor_id = data.pop('professor_id')
        if professor_id:
            professor = Professores.query.filter(Professores.id==professor_id).first
            prova.professor = professor

        questoes_ids = data.pop('questoes_ids')
        if questoes_ids:
            questoes = Questoes.query.filter(Questoes.id.in_(questoes_ids)).all()
            prova.questoes = questoes

        for key, value in data.items():
            setattr(prova, key, value)

        prova.save()

        return schema.dump(prova), 200