from flask import Blueprint
from app.controllers.questoes_controller import QuestoesList, QuestoesDetail

questoes_api = Blueprint('questoes_api', __name__)

questoes_api.add_url_rule(
    '/questoes', view_func=QuestoesList.as_view('questoes_list'), methods=['POST', 'GET']
)

questoes_api.add_url_rule(
    '/questao/<int:questao_id>', view_func=QuestoesDetail.as_view('questao_detail'), methods=['GET', 'DELETE', 'PATCH']
)