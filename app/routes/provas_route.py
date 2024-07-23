from flask import Blueprint
from app.controllers.provas_controller import ProvasList, ProvasDetail

provas_api = Blueprint('provas_api', __name__)

provas_api.add_url_rule(
    '/provas', view_func=ProvasList.as_view('provas_list'), methods=['POST', 'GET']
)

provas_api.add_url_rule(
    '/prova/<int:prova_id>', view_func=ProvasDetail.as_view('prova_detail'), methods=['GET', 'DELETE', 'PATCH']
)