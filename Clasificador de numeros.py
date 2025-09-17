# --- Función para verificar si un número es primo ---
def es_primo(numero):
    """Verifica si un número es primo"""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# --- Clasificador de números ---
def clasificar_numeros():
    print("=== CLASIFICADOR DE NÚMEROS ===")
    print("Escriba números enteros uno por uno. Para salir escriba 0.\n")

    pares = []
    impares = []
    primos = []

    while True:
        numero = int(input("Número: "))

        if numero == 0:
            break

        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

        if es_primo(numero):
            primos.append(numero)

    # --- Resultados ---
    print("\n--- RESULTADOS ---")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Primos: {primos}")


# Ejecutar
clasificar_numeros()
