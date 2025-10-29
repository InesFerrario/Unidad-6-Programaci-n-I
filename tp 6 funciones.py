#EJERCICIO 1
#def imprimir_hola_mundo ():
#    print("Hola Mundo!")

#imprimir_hola_mundo()


#EJERCICIO 2
#def saludar_usuario(nombre):
#    saludo= "Hola " + nombre + " !"
#    return saludo

#nombre_ingresado = input("Por favor, ingresa tu nombre: ")

#mensaje= saludar_usuario(nombre_ingresado)

#print(mensaje)


#EJERCICIO 3
#def informacion_personal(nombre, apellido, edad, residencia):
#    print ("Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia + ".")
  
#nombre_usuario= input ("Ingresa tu nombre: ")
#apellido_usuario= input ("Ingresa tu apellido: ")
#edad_usuario= input("Ingresa tu edad: ")
#residencia_usuario= input("Ingresa tu lugar de residencia: ")

#informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#EJERCICIO 4
#import math

#def calcular_area_circulo(radio):
#    area= math.pi * (radio**2)
#    return area

#def calcular_perimetro_circulo(radio):
#    perimetro= 2 * math.pi * radio
#    return perimetro

#radio_usuario = float(input("Ingresa el radio del círculo: "))

#area_resultado= calcular_area_circulo(radio_usuario)
#perimetro_resultado = calcular_perimetro_circulo(radio_usuario)

#print("El área del círculo es: ", area_resultado)
#print("El perímetro del círculo es: ", perimetro_resultado)


#EJERCICIO 5
#def segundos_a_horas(segundos):
#    horas = segundos / 3600
#    return horas

#segundos_usuario = int(input("Ingresa la cantidad de segundos: "))

#resultado_horas = segundos_a_horas(segundos_usuario)

#print("Equivale a ", resultado_horas, "horas.")


#EJERCICIO 6
#def tabla_multiplicar(numero):
#    for i in range(1,11):
#        resultado = numero * i
#        print(numero, " x ", i , " = ", resultado)

#numero_usuario = int(input("Inresa un número. Verás su tabla de multiplicar: "))

#tabla_multiplicar(numero_usuario)


#EJERCICIO 7
#def operaciones_basicas(a, b):
#    suma = a + b
#    resta = a - b
#    multiplicacion = a * b
#    division = a / b
#    return (suma , resta , multiplicacion , division)

#numero1= float(input("Ingresa el primer número: "))
#numero2= float(input("Ingresa el segundo número: "))

#resultados = operaciones_basicas(numero1, numero2)

#print("Suma: ", resultados[0])
#print("Resta: ", resultados[1])
#print("Multiplicación: ", resultados[2])
#print("División: ", resultados[3])


#EJERCICIO 8
#def calcular_imc (peso, altura):
#    imc = peso / (altura ** 2)
#    return imc

#peso_usuario = float(input("Ingresa tu peso en kg: "))
#altura_usuario = float(input("Ingresa tu altura en metros: "))

#resultado_imc = calcular_imc(peso_usuario , altura_usuario)

#print("Tu IMC es:", round(resultado_imc, 2))


#EJERCICIO 9
#def celcius_a_fahrenheit (celcius):
#    fahrenheit = (celcius * 9/5) + 32
#    return fahrenheit

#temp_celcius = float (input("Ingresa la temperatura, expresada en grados Celcius: "))

#temp_fahrenheit= celcius_a_fahrenheit(temp_celcius)

#print("La temperatura en Fahrenheit es: ", temp_fahrenheit)


#EJERCICIO 10
#def calcular_promedio (a,b,c):
#    promedio = (a + b + c) / 3
#    return promedio

#numero1= float(input("Ingresa la primera nota: "))
#numero2= float(input("Ingresa la segunda nota: "))
#numero3= float(input("Ingresa la tercera nota: "))

#resultado_promedio= calcular_promedio (numero1, numero2 , numero3)

#print ("El promedio es: ", resultado_promedio)

