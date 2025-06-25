from flask import Blueprint, request, jsonify
from app import db
from app.models import OfertaLaboral

bp_ofertas = Blueprint('ofertas', __name__, url_prefix='/ofertas')

@bp_ofertas.route('/', methods=['GET'])
def listar_ofertas():
    ofertas = OfertaLaboral.query.all()
    return jsonify([{
        'id': o.id,
        'cliente': o.cliente,
        'cargo': o.cargo,
        'descripcion': o.descripcion,
        'ciudad': o.ciudad
    } for o in ofertas])

@bp_ofertas.route('/', methods=['POST'])
def crear_oferta():
    data = request.get_json()
    oferta = OfertaLaboral(
        cliente=data['cliente'],
        cargo=data['cargo'],
        descripcion=data.get('descripcion'),
        ciudad=data.get('ciudad')
    )
    db.session.add(oferta)
    db.session.commit()
    return jsonify({'mensaje': 'Oferta creada', 'id': oferta.id}), 201

@bp_ofertas.route('/<int:id>', methods=['PUT'])
def actualizar_oferta(id):
    data = request.get_json()
    oferta = OfertaLaboral.query.get_or_404(id)

    oferta.cliente = data.get('cliente', oferta.cliente)
    oferta.cargo = data.get('cargo', oferta.cargo)
    oferta.descripcion = data.get('descripcion', oferta.descripcion)
    oferta.ciudad = data.get('ciudad', oferta.ciudad)

    db.session.commit()
    return jsonify({'mensaje': 'Oferta actualizada'})

@bp_ofertas.route('/<int:id>', methods=['DELETE'])
def eliminar_oferta(id):
    oferta = OfertaLaboral.query.get_or_404(id)
    db.session.delete(oferta)
    db.session.commit()
    return jsonify({'mensaje': 'Oferta eliminada'})
