from flask import Blueprint, request, jsonify
from app import db
from app.models import Asociacion, Candidato, OfertaLaboral, OrdenContratacion
from datetime import datetime

bp_asociaciones = Blueprint('asociaciones', __name__, url_prefix='/asociaciones')

# Crear una asociación entre candidato, oferta y orden (orden opcional)
@bp_asociaciones.route('/', methods=['POST'])
def crear_asociacion():
    data = request.get_json()
    
    candidato_id = data.get('candidato_id')
    oferta_id = data.get('oferta_id')
    orden_id = data.get('orden_id')  # opcional

    candidato = Candidato.query.get_or_404(candidato_id)
    oferta = OfertaLaboral.query.get_or_404(oferta_id)
    orden = OrdenContratacion.query.get(orden_id) if orden_id else None

    asociacion = Asociacion(
        candidato_id=candidato.id,
        oferta_id=oferta.id,
        orden_id=orden.id if orden else None,
        fecha_asociacion=datetime.utcnow()
    )

    db.session.add(asociacion)
    db.session.commit()

    return jsonify({'mensaje': 'Asociación creada', 'id': asociacion.id}), 201

# Obtener todas las asociaciones
@bp_asociaciones.route('/', methods=['GET'])
def listar_asociaciones():
    asociaciones = Asociacion.query.all()
    resultado = []

    for a in asociaciones:
        resultado.append({
            'id': a.id,
            'candidato_id': a.candidato.id,
            'candidato': f"{a.candidato.nombre} {a.candidato.apellido}",
            'cedula': a.candidato.cedula,
            'ciudad_domicilio': a.candidato.ciudad_domicilio,  # 👈 AGREGA ESTO
            'oferta': a.oferta.cargo,
            'cliente': a.oferta.cliente,
            'orden': a.orden.cargo if a.orden else None,
            'fecha_asociacion': a.fecha_asociacion.isoformat()
        })

    return jsonify(resultado)
