#Practica 1 

 # Programa sencillo de validación de contraseña

contraseña_valida = input("Define la contraseña válida: ").strip()

intentos = 3
while intentos > 0:
    clave = input("Escribe tu contraseña: ").strip()
    if clave == contraseña_valida:
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        else:
            print("Has agotado los intentos. Acceso denegado")