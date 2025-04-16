# 1- 

def imprimir_hola_mundo():
    print("Hola mundo!")
    
# imprimir_hola_mundo()



# 2-

def saludar():
    nombre = input("Cuál es tu nombre? ")
    def saludar_usuario(nombre_usr):
        print(f"Hola, {nombre_usr}")
    saludar_usuario(nombre)

# saludar()



# 3-

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") 

# nombre = input("Ingresa tu nombre: ")
# apellido = input("Ingresa tu apellido: ")
# edad = input("Ingresa tu edad: ")
# residencia = input("Ingresa tu lugar de residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)



# 4-

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio * radio)
    print(area)
  
def calcular_perimetro_circulo(radio):
    perimetro =  2 * math.pi * radio 
    print(perimetro)
  
# calcular_area_circulo(5)
# calcular_perimetro_circulo(5)



# 5-

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
    
# segundos_introducidos = int(input("Ingrese la cantidad de segundos a convertir a horas: "))
# segundos_a_horas(segundos_introducidos)



# 6-

def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{numero} * {i} = {numero * i}")

# numero_introducido = int(input("Ingrese el número del que desea saber su tabla: "))
# tabla_multiplicar(numero_introducido)



# 7-

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b 
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero!"
    return (suma, resta, multiplicacion, division)

# a = float(input("Ingresa el primer número: "))
# b = float(input("Ingresa el segundo número: "))

# resultados = operaciones_basicas(a, b)

# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")



# 8-

def calcular_imc(peso, altura):
    IMC = round(peso / (altura * altura), 2)
    print(f"El índice de masa corporal es {IMC}")
    
# peso_ingresado = float(input("Ingrese su peso: "))
# altura_ingresada = float(input("Ingrese su altura: "))
    
# indice_masa_corporal = calcular_imc(peso_ingresado, altura_ingresada)



# 9-

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# celsius_ingresados = float(input("Ingrese la temperatura en grados Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celsius_ingresados)



# 10-

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los números ingresados es: {promedio:.2f}")
    
# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# num3 = float(input("Ingresa el tercer número: "))
# promedio_final = calcular_promedio(num1, num2, num3)