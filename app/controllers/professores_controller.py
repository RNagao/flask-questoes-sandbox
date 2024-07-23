from flask import request
from flask.views import MethodView

from app.models.professores_model import Professores
from app.models.provas_model import Provas
from app.schemas.professores_schema import ProfessoresSchema

class ProfessoresList(MethodView):
    def post(self):
        data = request.get_json(force=True)
        schema = ProfessoresSchema()

        provas_ids = data.pop('provas_ids', [])
        provas = Provas.query.filter(Provas.id.in_(provas_ids)).all()

        professor = schema.load(data)
        professor.provas = provas

        professor.save()

        return schema.dump(professor), 201

    def get(self):
        professores = Professores.query.all()
        schema = ProfessoresSchema(many=True)
        return schema.dump(professores)
    
class ProfessorDetail(MethodView):
    def get(self, professor_id):
        professor = Professores.query.filter_by(id=professor_id).first_or_404()
        schema = ProfessoresSchema()
        return schema.dump(professor), 200
    
    def delete(self, professor_id):
        professor = Professores.query.filter_by(id=professor_id).first_or_404()
        professor.delete(professor)
        return {}, 204

    def patch(self, professor_id):
        data = request.get_json(force=True)
        schema = ProfessoresSchema(partial=True)
        professor = Professores.query.filter_by(id=professor_id).first_or_404()

        provas_ids = data.pop('provas_ids', [])
        if provas_ids:
            provas = Provas.query.filter(Provas.id.in_(provas_ids)).all()
            professor.provas = provas

        for key, value in data.items():
            setattr(professor, key, value)

        professor.save()

        return schema.dump(professor), 200