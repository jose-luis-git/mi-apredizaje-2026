const form = document.querySelector("form");
const mensaje = document.querySelector("#mensaje");
const tbody = document.querySelector("#tabla-personas tbody");
const btnLimpiar = document.querySelector("#btn-limpiar");

async function actualizar_tabla() {
    const res = await fetch("/persona");
    const personas = await res.json();

    tbody.innerHTML = "";

    personas.forEach(persona => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${persona.id}</td>
            <td>${persona.nombre}</td>
            <td>${persona.edad}</td>
            <td><button class="btn-eliminar" data-id="${persona.id}">Eliminar</button></td>
        `;
        tbody.appendChild(tr);
    });

    document.querySelectorAll(".btn-eliminar").forEach(btn => {
    btn.addEventListener("click", async() => {
        const id = btn.getAttribute("data-id");
        if(confirm(`¿Desea eliminar a la persona con ID ${id}?`)){
            const res = await fetch(`/persona/${id}`, {
                method: "DELETE"
            });
            const data = await res.json();
            alert(data.mensaje);
            actualizar_tabla();
        }
    });
});
}

actualizar_tabla();


form.addEventListener("submit", async(e) => {
    e.preventDefault();

    const nombre = document.querySelector("#nombre").value;
    const edad = document.querySelector("#edad").value;

    const res = await fetch("/persona", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            nombre: nombre,
            edad: edad
        })
    });
    const data = await res.json();
    mensaje.textContent = data.mensaje;

    form.reset();
    actualizar_tabla();
});

btnLimpiar.addEventListener("click", async() => {
    if(confirm("¿Desea eliminar todos los registros?")){
        const res = await fetch("/persona", {
            method: "DELETE"
        });
        const data = await res.json();
        alert(data.mensaje);
        actualizar_tabla();
    }
});