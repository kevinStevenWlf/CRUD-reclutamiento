from flask import Blueprint, request, jsonify
from app import db
from app.models import OrdenContratacion

bp_ordenes = Blueprint('ordenes', __name__, url_prefix='/ordenes')

@bp_ordenes.route('/', methods=['GET'])
def listar_ordenes():
    ordenes = OrdenContratacion.query.all()
    return jsonify([{
        'id': o.id,
        'cliente': o.cliente,
        'cargo': o.cargo,
        'examenes': o.examenes
    } for o in ordenes])

@bp_ordenes.route('/', methods=['POST'])
def crear_orden():
    data = request.get_json()
    orden = OrdenContratacion(
        cliente=data['cliente'],
        cargo=data['cargo'],
        examenes=data.get('examenes')
    )
    db.session.add(orden)
    db.session.commit()
    return jsonify({'mensaje': 'Orden creada', 'id': orden.id}), 201

@bp_ordenes.route('/<int:id>', methods=['PUT'])
def actualizar_orden(id):
    data = request.get_json()
    orden = OrdenContratacion.query.get_or_404(id)

    orden.cliente = data.get('cliente', orden.cliente)
    orden.cargo = data.get('cargo', orden.cargo)
    orden.examenes = data.get('examenes', orden.examenes)

    db.session.commit()
    return jsonify({'mensaje': 'Orden actualizada'})

@bp_ordenes.route('/<int:id>', methods=['DELETE'])
def eliminar_orden(id):
    orden = OrdenContratacion.query.get_or_404(id)
    db.session.delete(orden)
    db.session.commit()
    return jsonify({'mensaje': 'Orden eliminada'})
