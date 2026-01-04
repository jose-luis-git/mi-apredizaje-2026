sesion_abierta = {
    "nombre" : "jose",
    "id" : "23"
}
session_cerrada = {}

def login_required(func):
    def wrapper(sesion, *args, **kwargs):
        if "nombre" not in sesion:
            print("Acceso denegado inicie sesion")
            return
        return func(sesion,*args, **kwargs)
    return wrapper


@login_required
def dashboard(sesion):
    print(f"Bienvenido {sesion["nombre"]} al dasboard")


print("-------PRUBEBA SESION CERRADA-------")
dashboard(session_cerrada)

print("-------PRUBEBA SESION ABIERTA-------")
dashboard(sesion_abierta)