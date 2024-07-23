from marshmallow import EXCLUDE
from app.extensions import ma
from app.models.questoes_model import Questoes

class QuestoesSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Questoes
        load_instance=True
        ordered=True
        unknown = EXCLUDE
    
    id = ma.auto_field(dump_only=True)
    pergunta = ma.auto_field(required=True)
    resposta = ma.auto_field(required=True)
    provas = ma.Nested('ProvasSchema', exclude=('questoes',), many=True)