from marshmallow import EXCLUDE
from app.extensions import ma
from app.models.provas_model import Provas

class ProvasSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Provas
        load_instance=True
        ordered=True
        unknown = EXCLUDE
    
    id = ma.auto_field(dump_only=True)
    descricao = ma.auto_field(required=True)
    professor_id = ma.auto_field(load_only=True)
    professor = ma.Nested('ProfessoresSchema', exclude=('provas',), many=False)
    questoes = ma.Nested('QuestoesSchema', exclude=('provas',), many=True)