document.addEventListener("DOMContentLoaded", ()=> {
    update_table();
});

const form = document.querySelector("form");
const message = document.querySelector("#message");
const tbody = document.querySelector("#table_user tbody");
const btn_clean = document.querySelector("#btn_clean");

let editingId = null;

async function update_table(){
    const res = await fetch("/user");
    const users = await res.json();

    tbody.innerHTML = "";

    const amount = document.querySelector("#amount");
        amount.textContent = users.length;

    users.forEach(user => {
        const tr = document.createElement("tr");
        
        tr.innerHTML = `
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.email}</td>
            <td class="actions">
                <button type="button" class="btn_edit" data-id="${user.id}">Edit</button>
            </td>
            <td class="actions">
                <button type="button" class="btn_delete" data-id="${user.id}">Delete</button>
            </td>  
        `;

        tbody.appendChild(tr);
    });

    document.querySelectorAll(".btn_edit").forEach(btn => {
        btn.disabled = false;
        btn.addEventListener("click", async ()=> {
            btn.disabled = true;
            const id = btn.getAttribute("data-id");

            const row = btn.closest("tr");
            const name = row.children[1].textContent;
            const email = row.children[2].textContent;

            editingId = id;

            document.querySelectorAll("tr").forEach(tr => {
                tr.classList.remove("editing");
            });

            row.classList.add("editing");

            document.querySelector("#name").value = name;
            document.querySelector("#email").value = email;

            document.querySelector("#btn_send").textContent = "Update";
            document.querySelector("#btn_cancel").hidden = false;
        });
    });

    document.querySelectorAll(".btn_delete").forEach(btn => {
        btn.addEventListener("click", async ()=> {
            const id = btn.getAttribute("data-id");

            if(confirm(`Do you wish delete de user get id=${id}?`)){
                const res = await fetch(`/user/${id}`, {
                    method: "DELETE"
                });
                const data = await res.json();

                alert(data.message);
                update_table();
            }
        });
    });
}

form.addEventListener("submit", async (e)=> {
    e.preventDefault();

    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;

    let url = "/user";
    let method = "POST";

    if(editingId !== null){
        url = `/user/${editingId}`;
        method = "PUT";
    }
    
    const res = await fetch(url, {
        method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            email: email
        })
    });

    const data = await res.json();

    message.textContent = data.message;

    resetForm();
    update_table();
});

btn_clean.addEventListener("click", async ()=> {
    if(confirm("Do you delete all users?")){
        const res = await fetch("/user", {
            method: "DELETE"
        })
        const data = await res.json();
        alert(data.message);

        update_table();
    }
});

document.querySelector("#btn_cancel").addEventListener("click", ()=> {
    resetForm();
});

function resetForm(){
    form.reset();
    editingId = null;

    document.querySelectorAll(".btn_edit").forEach(btn => {
        btn.disabled = false;
    });
    document.querySelectorAll("tr").forEach(tr => {
        tr.classList.remove("editing")
    });
    document.querySelector("#btn_send").textContent = "Send";
    document.querySelector("#btn_cancel").hidden = true;
}