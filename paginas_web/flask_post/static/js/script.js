const form = document.querySelector("form");
const mensaje = document.querySelector("#mensaje");

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
});