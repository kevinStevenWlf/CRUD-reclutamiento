from app.routes.candidatos import bp_candidatos
from app.routes.ofertas import bp_ofertas
from app.routes.ordenes import bp_ordenes
from app.routes.asociaciones import bp_asociaciones

def register_blueprints(app):
    app.register_blueprint(bp_candidatos)
    app.register_blueprint(bp_ofertas)
    app.register_blueprint(bp_ordenes)
    app.register_blueprint(bp_asociaciones)
