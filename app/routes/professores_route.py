from flask import Blueprint
from app.controllers.professores_controller import ProfessoresList, ProfessorDetail

professores_api = Blueprint('professores_api', __name__)

professores_api.add_url_rule(
    '/professores', view_func=ProfessoresList.as_view('professores_list'), methods=['POST', 'GET']
)

professores_api.add_url_rule(
    '/professor/<int:professor_id>', view_func=ProfessorDetail.as_view('professor_detail'), methods=['GET', 'DELETE', 'PATCH']
)