# 1-

# for i in range (100, 0, -1):
#     print(i)



# 2- 

# numero = input("Ingrese el número deseado: ")
# digitos = len(numero)
# print(f'Su número tiene {digitos} digito/s')



# 3-

# num1 = int(input("Ingrese el primer valor (entero): "))
# num2 = int(input("Ingrese el segundo valor (entero): "))
# contador = 0

# for i in range (num1 + 1, num2):
#     contador = contador + i
# print(f'La suma de los valores comprendidos entre los números ingresados es: {contador}')



# 4-

# contador = 0
# num = 1
# while num != 0:
#     num = int(input("Ingrese el número deseado (presione 0 para detener la cuenta): "))
#     contador = contador + num
# print(f'La cuenta total de números ingresados da: {contador}')



# 5-

# import random
# rand = random.randint(1, 10)
# num = -1
# contador = 0

# while num != rand:
#     num = int(input("Ingrese el número que cree que es: "))
#     contador += 1
# print(f'Adivinaste! Te tomó {contador} intento/s')



# 6-

# for i in range (100, -1, -2):
#      print(i)



# 7-

# acumulador = 0
# num = int(input("Ingrese el número deseado: "))

# for i in range(1, num + 1):
#     acumulador = acumulador + i
# print(f'La suma desde 0 hasta el número {num} es: {acumulador}')



# 8-

# pares = 0
# impares = 0
# negativos = 0
# positivos = 0

# for i in range(100):
#     num = int(input(f'ingrese el número deseado ({i + 1}): '))
#     if num > 0:
#         positivos += 1
#     else:
#         negativos += 1
    
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print(f"Del total, hay {pares} números pares, {impares} impares, {positivos} positivos y {negativos} negativos")



# 9-

# MAX = 4
# contador = 0

# for i in range(MAX):
#     num = int(input(f"Ingrese el número deseado ({i + 1}): "))
#     contador = contador + num
# print(f"El promedio de los {MAX} números ingresado es: {contador / MAX}")



# 10-

# numero = input("Ingrese el número deseado: ")

# numero_invertido = ""

# for digito in numero:
#     numero_invertido = digito + numero_invertido
# print(f"{numero} invertido es: {numero_invertido}")