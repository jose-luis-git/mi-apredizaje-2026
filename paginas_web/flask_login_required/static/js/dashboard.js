const btn_cancel = document.querySelector("#btn_logout");

btn_cancel.addEventListener("click", async() => {
    const res = await fetch("/logout", {
        method: "POST"
    });
    
    window.location.href = "/";
});