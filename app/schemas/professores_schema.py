from marshmallow import EXCLUDE
from app.models.professores_model import Professores
from app.extensions import ma

class ProfessoresSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professores
        load_instance=True
        ordered=True
        unknown = EXCLUDE

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)
    provas = ma.Nested('ProvasSchema', exclude=('professor',), many=True)
