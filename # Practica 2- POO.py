# Clase Padre
class Vehiculo:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
    def encender(self):
        print(f"El vehículo {self.marca} {self.modelo} está encendido.")

    def apagar(self):
        print(f"El vehículo {self.marca} {self.modelo} está apagado.")


# Clase Hija 1
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre
        self.puertas = puertas           # Atributo propio

    def tocar_bocina(self):
        print("Beep beep!")

# Clase Hija 2
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Atributo propio (por ejemplo: deportiva, scooter)

    def hacer_caballito(self):
        print(f"La motocicleta {self.marca} hace un caballito.")



auto1 = Automovil("Toyota", "Corolla", 4)
moto1 = Motocicleta("Yamaha", "MT-07", "deportiva")


auto1.encender()
moto1.encender()


auto1.tocar_bocina()
moto1.hacer_caballito()


print(f"El auto tiene {auto1.puertas} puertas.")
print(f"La moto es de tipo {moto1.tipo}.")


# Se crea un objeto de la clase Automovil con marca, modelo y cantidad de puertas
auto1 = Automovil("Toyota", "Corolla", 4)

# Se enciende el auto usando el método heredado de Vehiculo
auto1.encender()

# Se llama a un método propio de la clase Automovil
auto1.tocar_bocina()


