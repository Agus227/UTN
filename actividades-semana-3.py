# 1-

# EDAD_MINIMA = 18
# edad = int(input("Ingrese su edad: "))
# if edad >= EDAD_MINIMA:
#     print("Es mayor de edad")
    
    

# 2-

# nota = int(input("Ingrese su nota: "))
# if nota > 5:
#     print("Aprobado")
# else: 
#     print("Desaprobado")



# 3-

# numero = int(input("Ingrese un número par: "))
# if numero % 2 == 0: 
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")



# 4-

# edad = int(input("Ingrese su edad: "))
# if edad < 12:
#     print("Niño")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad > 17 and edad < 30:
#     print("Adulto/a jóven")
# else: 
#     print("Adulto")



# 5-

# contraseña = input("Ingrese una contraseña: ")
# if len(contraseña) > 7 and len(contraseña) < 15:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# 6-

# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo (derecha)")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo (izquierda)")
# else:
#     print("Sin sesgo")



# 7-

# palabra_frase = input("Ingrese una palabra o frase: ")
# if palabra_frase.endswith(("a", "e", "i", "o", "u")):
#     palabra_frase += "!"
#     print(palabra_frase)
# else: print(palabra_frase)



# 8-

# nombre = input("Ingrese su nombre: ")
# decision = input("Cómo quiere ver su nombre? pulse 1 para mayúscula, 2 para minúscula, 3 para primera letra mayúscula: ")

# if decision == "1":
#     print(nombre.upper())
# elif decision == "2":
#     print(nombre.lower())
# else: print(nombre.title())



# 9-

# magnitud = int(input("Ingrese la magnitud del terremoto: "))

# if magnitud < 3:
#     print("Muy leve")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy fuerte")
# else: print("Extremo")



# 10-

# hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
# while hemisferio not in ["N", "S"]:
#     hemisferio = input("Entrada no válida. Ingrese 'N' para hemisferio norte o 'S' para hemisferio sur: ").upper()

# mes = int(input("Ingrese el número del mes (1-12): "))
# while not (1 <= mes <= 12):
#     mes = int(input("Número de mes inválido. Ingrese un número entre 1 y 12: "))

# dia = int(input("Ingrese el día del mes: "))
# while not (1 <= dia <= 31):
#     dia = int(input("Número de día inválido. Ingrese un número entre 1 y 31: "))

# if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and not (mes == 3 and dia > 20)):
#     estacion = "Invierno" if hemisferio == "N" else "Verano"
# elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and not (mes == 6 and dia > 20)):
#     estacion = "Primavera" if hemisferio == "N" else "Otoño"
# elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and not (mes == 9 and dia > 20)):
#     estacion = "Verano" if hemisferio == "N" else "Invierno"
# else:
#     estacion = "Otoño" if hemisferio == "N" else "Primavera"

# print(f"Usted se encuentra en la estación: {estacion}")