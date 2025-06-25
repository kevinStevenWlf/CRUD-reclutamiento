from flask import Blueprint, request, jsonify
from app import db
from app.models import Candidato
from datetime import datetime

bp_candidatos = Blueprint('candidatos', __name__, url_prefix='/candidatos')

@bp_candidatos.route('/', methods=['GET'])
def listar_candidatos():
    candidatos = Candidato.query.all()
    return jsonify([{
        'id': c.id,
        'nombre': c.nombre,
        'apellido': c.apellido,
        'tipo_documento': c.tipo_documento,
        'cedula': c.cedula,
        'fecha_nacimiento': c.fecha_nacimiento.isoformat(),
        'rh': c.rh,
        'ciudad_expedicion': c.ciudad_expedicion,
        'ciudad_nacimiento': c.ciudad_nacimiento,
        'ciudad_domicilio': c.ciudad_domicilio
    } for c in candidatos])

@bp_candidatos.route('/', methods=['POST'])
def crear_candidato():
    data = request.get_json()
    candidato = Candidato(
        nombre=data['nombre'],
        apellido=data['apellido'],
        tipo_documento=data['tipo_documento'],
        cedula=data['cedula'],
        fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date(),
        rh=data.get('rh'),
        ciudad_expedicion=data.get('ciudad_expedicion'),
        ciudad_nacimiento=data.get('ciudad_nacimiento'),
        ciudad_domicilio=data.get('ciudad_domicilio')
    )
    db.session.add(candidato)
    db.session.commit()
    return jsonify({'mensaje': 'Candidato creado', 'id': candidato.id}), 201

@bp_candidatos.route('/<int:id>', methods=['GET'])
def obtener_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    return jsonify({
        'id': candidato.id,
        'nombre': candidato.nombre,
        'apellido': candidato.apellido,
        'tipo_documento': candidato.tipo_documento,
        'cedula': candidato.cedula,
        'fecha_nacimiento': candidato.fecha_nacimiento.isoformat(),
        'rh': candidato.rh,
        'ciudad_expedicion': candidato.ciudad_expedicion,
        'ciudad_nacimiento': candidato.ciudad_nacimiento,
        'ciudad_domicilio': candidato.ciudad_domicilio
    })

@bp_candidatos.route('/<int:id>', methods=['PUT'])
def actualizar_candidato(id):
    data = request.get_json()
    candidato = Candidato.query.get_or_404(id)

    candidato.nombre = data.get('nombre', candidato.nombre)
    candidato.apellido = data.get('apellido', candidato.apellido)
    candidato.tipo_documento = data.get('tipo_documento', candidato.tipo_documento)
    candidato.cedula = data.get('cedula', candidato.cedula)
    candidato.fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date()
    candidato.rh = data.get('rh', candidato.rh)
    candidato.ciudad_expedicion = data.get('ciudad_expedicion', candidato.ciudad_expedicion)
    candidato.ciudad_nacimiento = data.get('ciudad_nacimiento', candidato.ciudad_nacimiento)
    candidato.ciudad_domicilio = data.get('ciudad_domicilio', candidato.ciudad_domicilio)

    db.session.commit()
    return jsonify({'mensaje': 'Candidato actualizado'})

@bp_candidatos.route('/<int:id>', methods=['DELETE'])
def eliminar_candidato(id):
    candidato = Candidato.query.get_or_404(id)
    db.session.delete(candidato)
    db.session.commit()
    return jsonify({'mensaje': 'Candidato eliminado'})
