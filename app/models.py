from app import db
from datetime import datetime

class Candidato(db.Model):
    __tablename__ = 'candidatos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    tipo_documento = db.Column(db.String(10), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    rh = db.Column(db.String(5))
    ciudad_expedicion = db.Column(db.String(100))
    ciudad_nacimiento = db.Column(db.String(100))
    ciudad_domicilio = db.Column(db.String(100))

    asociaciones = db.relationship('Asociacion', backref='candidato', lazy=True)


class OfertaLaboral(db.Model):
    __tablename__ = 'ofertas_laborales'

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    ciudad = db.Column(db.String(100))

    asociaciones = db.relationship('Asociacion', backref='oferta', lazy=True)


class OrdenContratacion(db.Model):
    __tablename__ = 'ordenes_contratacion'

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    examenes = db.Column(db.Text)

    asociaciones = db.relationship('Asociacion', backref='orden', lazy=True)


class Asociacion(db.Model):
    __tablename__ = 'asociaciones'

    id = db.Column(db.Integer, primary_key=True)
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidatos.id'), nullable=False)
    oferta_id = db.Column(db.Integer, db.ForeignKey('ofertas_laborales.id'), nullable=False)
    orden_id = db.Column(db.Integer, db.ForeignKey('ordenes_contratacion.id'), nullable=True)
    fecha_asociacion = db.Column(db.DateTime, default=datetime.utcnow)
