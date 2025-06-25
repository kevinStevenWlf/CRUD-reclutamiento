# 🧠 Aplicación de Reclutamiento - Gestión de Talento Humano

Esta es una aplicación web fullstack construida con **Python (Flask)** para el backend y **HTML, CSS y JavaScript puro** para el frontend. Está diseñada para gestionar el proceso de reclutamiento y contratación de talento humano, incluyendo:

- Registro de candidatos
- Gestión de ofertas laborales
- Administración de órdenes de contratación
- Asociación de candidatos con ofertas y órdenes
- Generación de reportes

---

## 📁 Estructura del proyecto

```
.
├── app/                   # Backend Flask
│   ├── __init__.py
│   ├── models.py
│   └── routes/
│       ├── candidatos.py
│       ├── ofertas.py
│       ├── ordenes.py
│       ├── asociaciones.py
│       └── __init__.py
├── frontend/              # Frontend estático
│   ├── index.html
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── data/
│   └── candidatos.json    # Datos de ejemplo
├── migrations/            # Migraciones de base de datos (Flask-Migrate)
├── data.db                # Base de datos SQLite
├── run.py                 # Punto de entrada del backend
├── config.py              # Configuración Flask
├── importar_json.py       # Script para cargar candidatos desde JSON
├── requirements.txt       # Dependencias
└── README.md
```

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/nombre-repositorio.git
cd nombre-repositorio
```

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Inicializa la base de datos:

```bash
set FLASK_APP=run.py
flask db init
flask db migrate -m "Inicial"
flask db upgrade
```

4. Ejecuta el backend:

```bash
python run.py
```

5. Abre el frontend con doble clic en `frontend/index.html` o sirve la carpeta con Live Server si usas VS Code.

---

## 🌐 Funcionalidades

| Módulo           | Funcionalidades                                                   |
|------------------|--------------------------------------------------------------------|
| Candidatos       | Crear, listar, actualizar, eliminar                                |
| Ofertas          | Crear, listar, actualizar, eliminar                                |
| Órdenes          | Crear, listar, actualizar, eliminar                                |
| Asociaciones     | Vincular candidato ↔ oferta ↔ orden                                |
| Reportes         | 5 reportes dinámicos: por candidato, ciudad, fecha, etc.           |

---

## 📦 Dependencias principales

- `Flask`
- `Flask-SQLAlchemy`
- `Flask-Migrate`
- `Flask-CORS`

---

## ✨ Créditos

Desarrollado por [Kevin Steven Pérez Pineda] para la prueba técnica de reclutamiento https://kevinstevenwlf.github.io/curriculum/.

---