
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()} {self.velocidad} Km/h, {self.cilindrada} cc"


def main():
    vehiculos = []
    n = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(n):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Datos del automóvil {i}: {vehiculo}")

if __name__ == "__main__":
    main()


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.nro_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)


print(particular)
print(carga)
print(bicicleta)
print(motocicleta)


print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")


import csv

def guardar_datos_csv(vehiculos):
    try:
        with open("vehiculos.csv", "w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__, vehiculo.__dict__])
        print("Datos guardados correctamente en vehiculos.csv")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def leer_datos_csv():
    try:
        with open("vehiculos.csv", "r") as archivo:
            archivo_csv = csv.reader(archivo)
            print("Lista de Vehiculos:")
            for vehiculo in archivo_csv:
                print(vehiculo)
    except Exception as e:
        print(f"Error al leer datos: {e}")


vehiculos = [particular, carga, bicicleta, motocicleta]
guardar_datos_csv(vehiculos)


leer_datos_csv()
