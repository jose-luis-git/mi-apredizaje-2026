addEventListener("DOMContentLoaded", update_table);

const form = document.querySelector("form");
const message = document.querySelector("#message");
const tbody = document.querySelector("#table_student tbody");
const btn_clean = document.querySelector("#btn_clean");

let editingId = null;

async function update_table(){
    const res = await fetch("/student");
    const students = await res.json();
    
    tbody.innerHTML = ""

    students.forEach(student => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.note}</td>
            <td><button class="btn_edit" data-id="${student.id}">Edit</button></td>
            <td><button class="btn_delete" data-id="${student.id}">Delete</button></td>
        `;

        tbody.appendChild(tr);
    });

    document.querySelectorAll(".btn_delete").forEach(btn => {
        btn.addEventListener("click", async() => {
            const id = btn.getAttribute("data-id");

            if(confirm(`¿Do you wish delete id: ${id}?`)){
                const res = await fetch(`/student/${id}`, {
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
            const id = btn.getAttribute("data-id");

            const row = btn.closest("tr");
            const name = row.children[1].textContent;
            const age = row.children[2].textContent;
            const note = row.children[3].textContent;

            editingId = id;

            document.querySelector("#name").value = name;
            document.querySelector("#age").value = age;
            document.querySelector("#note").value = note;

            document.querySelector("#btn_send").textContent = "Update";
            document.querySelector("#btn_cancel").hidden = false;
        });
    });
}

update_table();

form.addEventListener("submit", async(e) => {
    e.preventDefault();

    const name = document.querySelector("#name").value;
    const age = document.querySelector("#age").value;
    const note = document.querySelector("#note").value;

    const url = editingId? `/student/${editingId}` : "/student";
    const method = editingId? "PUT" : "POST";

    const res = await fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            age: age,
            note: note
        })
    });

    const data = await res.json();

    message.textContent = data.message;

    resetForm();
    update_table();
});

btn_clean.addEventListener("click", async() => {
    if(confirm("¿Do you wish delete all?")){
        const res = await fetch("/student", {
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
    document.querySelector("#btn_send").innerHTML = "Send";
    document.querySelector("#btn_cancel").hidden = true;
}