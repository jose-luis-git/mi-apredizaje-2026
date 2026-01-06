const form = document.querySelector("form");
const message = document.querySelector("#message");
const tbody = document.querySelector("#table_person tbody");
const btnClear = document.querySelector("#btn_clean");

let editingId = null;

async function update_table(){
    const res = await fetch("/person");
    const people = await res.json();

    tbody.innerHTML = "";

    people.forEach(person => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${person.id}</td>
            <td>${person.name}</td>
            <td>${person.age}</td>
            <td><button class="btn_edit" data-id="${person.id}">Edit</button></td>
            <td><button class="btn_delete" data-id="${person.id}">Delete</button></td>
        `;
        tbody.appendChild(tr);
    });

    document.querySelectorAll(".btn_delete").forEach(btn => {
        btn.addEventListener("click", async() => {
            const id = btn.getAttribute("data-id");

            if(confirm(`Do you wish delete id: ${id}?`)){
                const res = await fetch(`/person/${id}`, {
                    method: "DELETE"
                });
                const data = await res.json();
                alert(data.message);
                update_table();
            }
        });
    });

    document.querySelectorAll(".btn_edit").forEach(btn => {
        btn.addEventListener("click", async() => {
            const id = btn.dataset.id;

            const row = btn.closest("tr");
            const name = row.children[1].textContent;
            const age  = row.children[2].textContent;

            editingId = id;

            document.querySelector("#name").value = name;
            document.querySelector("#age").value = age;

            document.querySelector("#send").textContent = "Update";
            document.querySelector("#btn_cancel").hidden = false;
        });           
    });
}

update_table();

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    console.log("Submit ejecutado");

    const name = document.querySelector("#name").value;
    const age = document.querySelector("#age").value;

    const url = editingId? `/person/${editingId}` : "/person";
    const method = editingId? "PUT" : "POST";

    const res = await fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            age: age
        })
    });
    const data = await res.json();
    message.textContent = data.message;

    resetForm();
    update_table();
});

btnClear.addEventListener("click", async() => {
    if(confirm(`Do you wish delete all?`)){
        const res = await fetch("/person", {
            method: "DELETE"
        });
        const data = await res.json();
        alert(data.message);

        update_table();
    }
});
document.querySelector("#btn_cancel").addEventListener("click", () => {
    resetForm();
});
function resetForm(){
    form.reset();
    editingId = null;
    document.querySelector("#send").textContent = "Send";
    document.querySelector("#btn_cancel").hidden = true;
}