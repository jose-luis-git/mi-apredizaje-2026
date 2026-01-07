const register = document.querySelector("#btn_register");
const login = document.querySelector("#btn_login");

register.addEventListener("click", ()=> {
    window.location.href = "/register";
});

login.addEventListener("click", ()=> {
    window.location.href = "/login";
});