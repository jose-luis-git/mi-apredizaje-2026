document.addEventListener("DOMContentLoaded", ()=> {
    update_table();
});

const form = document.querySelector("form");
const tbody = document.querySelector("#table_person tbody");
const message = document.querySelector("#message");
const btn_clean = document.querySelector("#btn_clean");
const btn_cancel = document.querySelector("#btn_cancel");

let editingId = null;

async function update_table() {
    const res = await fetch("/person");
    const people = await res.json();

    tbody.innerHTML = "";

    const amount = document.querySelector("#amount");
    amount.textContent = people.length;

    people.forEach(p => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>${p.age}</td>
            <td>${p.note}</td>
            <td class="actions">
                <button type="button" class="btn edit btn_edit" data-id="${p.id}">Edit</button>
            </td>
            <td>
                <button type=button class="btn delete btn_delete" data-id=${p.id}>Delete</button>
            </td>
        `;

        tbody.appendChild(tr);
    });
}

tbody.addEventListener("click", async(e) => {
    const btn_edit = e.target.closest(".btn_edit");
    const btn_delete = e.target.closest(".btn_delete");

    if(btn_edit){
        const row = btn_edit.closest("tr");
        const id = btn_edit.dataset.id;

        editingId = id;

        document.querySelectorAll(".btn_edit").forEach(btn => {
            btn.disabled = true;
        });

        document.querySelectorAll("tr").forEach(tr => {
            tr.classList.remove("editing");
        });
        row.classList.add("editing");

        document.querySelector("#name").value = row.children[1].textContent;
        document.querySelector("#age").value = row.children[2].textContent;
        document.querySelector("#note").value = row.children[3].textContent;

        document.querySelector("#btn_send").textContent = "Update";
        document.querySelector("#btn_cancel").hidden = false;

    }
    if(btn_delete){
        const id =  btn_delete.dataset.id;

        if(!confirm(`Delete person with id ${id}?`)) return;
        if(!confirm("This action cannot be undone")) return;
        
        const res = await fetch(`/person/${id}`, {
            method: "DELETE"
        });
        const data = await res.json();

        message.textContent = data.message;
        update_table();
    }
});

form.addEventListener("submit", async(e) => {
    e.preventDefault();

    const name = document.querySelector("#name").value;
    const age = document.querySelector("#age").value;
    const note = document.querySelector("#note").value;

    let url = "/person";
    let method = "POST";

    const isUpdate = editingId !== null;

    if(isUpdate){
        url = `/person/${editingId}`;
        method = "PUT";
    }

    const res = await fetch(url, {
        method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: name,
            age: age,
            note: note
        })
    });

    const data = await res.json();

    message.textContent = data.message;

    if(res.ok){
        resetForm();
    }

    update_table();
});

btn_clean.addEventListener("click", async()=>{
    if(confirm("Are you sure you want to delete everything?")){
        if(confirm("The changes are arriversible, are you sure?")){
            const res = await fetch("/person", {
                method: "DELETE"
            })
            const data = await res.json();
            alert(data.message);
            message.textContent = data.message;

            update_table();
        }
    }
});

btn_cancel.addEventListener("click", ()=> {
    resetForm();
});

function resetForm(){
    form.reset();

    editingId = null;

    document.querySelectorAll(".btn_edit").forEach(btn => {
        btn.disabled = false;
    });
    document.querySelectorAll("tr").forEach(tr => {
        tr.classList.remove("editing");
    });

    document.querySelector("#btn_send").textContent = "Send";
    document.querySelector("#btn_cancel").hidden = true;
}

const btn_up = document.querySelector("#scrollTop");

window.addEventListener("scroll", ()=> {
    btn_up.style.display = window.scrollY > 200? "block": "none";
});

btn_up.addEventListener("click", ()=> {
    window.scrollTo({top: 0, behavior: "smooth"});
});