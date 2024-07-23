from flask import Flask

from app.models.association_tables import provas_questoes
from app.routes.professores_route import professores_api
from app.routes.provas_route import provas_api
from app.routes.questoes_route import questoes_api
from .extensions import db, migrate, ma, cors
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    ma.init_app(app)
    cors.init_app(app, resources={r"/*":{"origins":"*"}})

    app.register_blueprint(professores_api)
    app.register_blueprint(provas_api)
    app.register_blueprint(questoes_api)

    return app
