from flask import request
from flask.views import MethodView

from app.models.questoes_model import Questoes
from app.models.provas_model import Provas
from app.schemas.questoes_schema import QuestoesSchema

class QuestoesList(MethodView):
    def post(self):
        data = request.get_json(force=True)
        schema = QuestoesSchema()

        data.pop('provas', None)
        provas_ids = data.pop('provas_ids', [])
        provas = Provas.query.filter(Provas.id.in_(provas_ids)).all()

        questao = schema.load(data)
        questao.provas = provas

        questao.save()

        return schema.dump(questao), 201

    def get(self):
        questoes = Questoes.query.all()
        schema = QuestoesSchema(many=True)
        return schema.dump(questoes)
    
class QuestoesDetail(MethodView):
    def get(self, questao_id):
        questao = Questoes.query.filter_by(id=questao_id).first_or_404()
        schema = QuestoesSchema()
        return schema.dump(questao), 200
    
    def delete(self, questao_id):
        questao = Questoes.query.filter_by(id=questao_id).first_or_404()
        questao.delete(questao)
        return {}, 204

    def patch(self, questao_id):
        data = request.get_json(force=True)
        provas_ids = data.pop('provas_ids', [])
        schema = QuestoesSchema(partial=True)
        questao = Questoes.query.filter_by(id=questao_id).first_or_404()

        for key, value in data.items():
            setattr(questao, key, value)

        if provas_ids:
            provas = Provas.query.filter(Provas.id.in_(provas_ids)).all()
            questao.provas = provas

        questao.save()

        return schema.dump(questao), 200