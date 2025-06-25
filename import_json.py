import json
from datetime import date
from app import create_app, db
from app.models import Candidato

app = create_app()

def importar_candidatos_desde_json(path):
    with app.app_context():
        with open(path, encoding='utf-8') as f:
            datos = json.load(f)

        for item in datos:
            candidato = Candidato(
                nombre=item.get("nombre", "").title(),
                apellido=item.get("apellido", "").title(),
                tipo_documento=item.get("clasE_DOCTO", "CC"),
                cedula=item.get("doctO_IDENT"),
                rh=item.get("grupO_RH"),
                ciudad_nacimiento=item.get("ciudad_n"),
                ciudad_expedicion=item.get("ciudad_e"),
                ciudad_domicilio=item.get("ciudad_d"),
                fecha_nacimiento=date(2000, 1, 1) 
            )
            db.session.add(candidato)

        db.session.commit()
        print(f"{len(datos)} candidatos importados correctamente.")

if __name__ == '__main__':
    importar_candidatos_desde_json("data/candidatos.json")
