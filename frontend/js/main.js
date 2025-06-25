function mostrarVista(vista) {
  const secciones = document.querySelectorAll('.vista');
  secciones.forEach(sec => sec.classList.remove('activa'));
  document.getElementById(`vista-${vista}`).classList.add('activa');
}

const apiUrl = "http://127.0.0.1:5000";

// FORMULARIO: Crear candidato
document.getElementById('form-candidato').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);
  data.fecha_nacimiento = new Date(data.fecha_nacimiento).toISOString().split('T')[0];

  const res = await fetch(`${apiUrl}/candidatos/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert("Candidato creado");
    e.target.reset();
    cargarCandidatos();
  } else {
    alert("Error al crear candidato");
  }
});

// Cargar lista de candidatos
async function cargarCandidatos() {
  const res = await fetch(`${apiUrl}/candidatos/`);
  const candidatos = await res.json();
  const tbody = document.querySelector('#tabla-candidatos tbody');
  tbody.innerHTML = "";
  candidatos.forEach(c => {
    const row = `<tr><td>${c.id}</td><td>${c.nombre}</td><td>${c.apellido}</td><td>${c.cedula}</td></tr>`;
    tbody.innerHTML += row;
  });
}

// Cargar automáticamente al iniciar
cargarCandidatos();

// FORMULARIO: Crear oferta laboral
document.getElementById('form-oferta').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  const res = await fetch(`${apiUrl}/ofertas/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert("Oferta creada");
    e.target.reset();
    cargarOfertas();
  } else {
    alert("Error al crear oferta");
  }
});

// FUNCION: Obtener ofertas desde API y listarlas en la tabla
async function cargarOfertas() {
  const res = await fetch(`${apiUrl}/ofertas/`);
  const ofertas = await res.json();
  const tbody = document.querySelector('#tabla-ofertas tbody');
  tbody.innerHTML = "";
  ofertas.forEach(o => {
    const row = `<tr><td>${o.id}</td><td>${o.cliente}</td><td>${o.cargo}</td><td>${o.ciudad}</td></tr>`;
    tbody.innerHTML += row;
  });
}

// Cargar ofertas automáticamente al abrir la app
cargarOfertas();


// FORMULARIO: Crear orden de contratación
document.getElementById('form-orden').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  const res = await fetch(`${apiUrl}/ordenes/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert("Orden creada");
    e.target.reset();
    cargarOrdenes();
  } else {
    alert("Error al crear orden");
  }
});

// FUNCION: Obtener órdenes desde API y listarlas
async function cargarOrdenes() {
  const res = await fetch(`${apiUrl}/ordenes/`);
  const ordenes = await res.json();
  const tbody = document.querySelector('#tabla-ordenes tbody');
  tbody.innerHTML = "";
  ordenes.forEach(o => {
    const row = `<tr><td>${o.id}</td><td>${o.cliente}</td><td>${o.cargo}</td><td>${o.examenes}</td></tr>`;
    tbody.innerHTML += row;
  });
}

// Cargar órdenes automáticamente
cargarOrdenes();


// Cargar selects con candidatos, ofertas y órdenes
async function cargarSelectsAsociacion() {
  const candidatos = await (await fetch(`${apiUrl}/candidatos/`)).json();
  const ofertas = await (await fetch(`${apiUrl}/ofertas/`)).json();
  const ordenes = await (await fetch(`${apiUrl}/ordenes/`)).json();

  const selectC = document.getElementById('select-candidato');
  const selectO = document.getElementById('select-oferta');
  const selectR = document.getElementById('select-orden');

  selectC.innerHTML = candidatos.map(c => `<option value="${c.id}">${c.nombre} ${c.apellido}</option>`).join('');
  selectO.innerHTML = ofertas.map(o => `<option value="${o.id}">${o.cargo} (${o.cliente})</option>`).join('');
  selectR.innerHTML = `<option value="">-- Sin orden --</option>` +
                      ordenes.map(r => `<option value="${r.id}">${r.cargo} (${r.cliente})</option>`).join('');
}

// Crear nueva asociación
document.getElementById('form-asociacion').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);
  if (data.orden_id === "") delete data.orden_id;

  const res = await fetch(`${apiUrl}/asociaciones/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (res.ok) {
    alert("Asociación creada");
    e.target.reset();
    cargarAsociaciones();
    cargarSelectsAsociacion();
  } else {
    alert("Error al asociar");
  }
});

// Listar asociaciones
async function cargarAsociaciones() {
  const res = await fetch(`${apiUrl}/asociaciones/`);
  const asociaciones = await res.json();
  const tbody = document.querySelector('#tabla-asociaciones tbody');
  tbody.innerHTML = "";
  asociaciones.forEach(a => {
    const row = `<tr>
      <td>${a.id}</td>
      <td>${a.candidato}</td>
      <td>${a.oferta}</td>
      <td>${a.cliente}</td>
      <td>${a.orden || "-"}</td>
      <td>${a.fecha_asociacion.split("T")[0]}</td>
    </tr>`;
    tbody.innerHTML += row;
  });
}

// Cargar automáticamente al iniciar
cargarAsociaciones();
cargarSelectsAsociacion();


async function reporteOfertasPorCandidato() {
  const id = document.getElementById('reporte-candidato-id').value;
  const res = await fetch(`${apiUrl}/asociaciones/`);
  const asociaciones = await res.json();
  const lista = document.getElementById('resultado-candidato');
  lista.innerHTML = "";

  asociaciones
    .filter(a => a.candidato_id == id) 
    .forEach(a => {
      lista.innerHTML += `<li>${a.candidato} → ${a.oferta} (${a.cliente})</li>`;
    });
}

async function reporteOrdenesClienteCiudad() {
  const res = await fetch(`${apiUrl}/ordenes/`);
  const ordenes = await res.json();
  const lista = document.getElementById('resultado-ordenes');
  lista.innerHTML = "";

  ordenes.forEach(o => {
    lista.innerHTML += `<li>${o.cliente} - ${o.cargo} (${o.examenes})</li>`;
  });
}

async function reporteCandidatosPorFecha() {
  const inicio = document.getElementById('fecha-inicio').value;
  const fin = document.getElementById('fecha-fin').value;
  const res = await fetch(`${apiUrl}/asociaciones/`);
  const asociaciones = await res.json();
  const lista = document.getElementById('resultado-fechas');
  lista.innerHTML = "";

  asociaciones.forEach(a => {
    const fecha = a.fecha_asociacion.split("T")[0];
    if (fecha >= inicio && fecha <= fin) {
      lista.innerHTML += `<li>${a.candidato} - ${a.cedula}</li>`;
    }
  });
}

async function reporteOfertasPorDocumento() {
  const res = await fetch(`${apiUrl}/candidatos/`);
  const candidatos = await res.json();
  const conteo = {};
  candidatos.forEach(c => {
    conteo[c.tipo_documento] = (conteo[c.tipo_documento] || 0) + 1;
  });

  const lista = document.getElementById('resultado-documentos');
  lista.innerHTML = "";
  for (let tipo in conteo) {
    lista.innerHTML += `<li>${tipo}: ${conteo[tipo]} ofertas</li>`;
  }
}

async function reporteCiudadDomicilio() {
  const ciudad = document.getElementById('ciudad-domicilio').value.trim().toLowerCase();
  const res = await fetch(`${apiUrl}/asociaciones/`);
  const asociaciones = await res.json();

  const lista = document.getElementById('resultado-ciudad');
  lista.innerHTML = "";

  asociaciones.forEach(a => {
    if (a.ciudad_domicilio && a.ciudad_domicilio.toLowerCase() === ciudad) {
      lista.innerHTML += `<li>${a.candidato} → ${a.oferta} (${a.cliente})</li>`;
    }
  });
}



