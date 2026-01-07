const form = document.querySelector("form");
const message = document.querySelector("#register_message");

form.addEventListener("submit", async(e) => {
    e.preventDefault();

    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;

    const res = await fetch("/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username,
            password: password
        })
    });

    const result = await res.json();
    message.textContent = result.message;

    if(result.success) form.reset();
});