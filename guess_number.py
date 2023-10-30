import random 

intentos = 0
minNumber = 1
maxNumber = 20

print("Hola usuario ¿Cual es tu nombre?")
username = input()

number = random.randint(minNumber, maxNumber)
print("Bueno, " + username + '. Estoy pensando en un numero entre ' + str(minNumber) + ' y ' + str(maxNumber))

while intentos < 6:
    print("Adivina: ")
    adivinar = input()
    adivinar = int(adivinar)


    intentos = intentos + 1

    if adivinar < number:
        print("Tu numero es demasiado bajo.")
    if adivinar > number:
        print("Tu numero es demasiado alto.")
    if adivinar == number:
        break

if adivinar == number:
    intentos = str(intentos)

    print("Bien hecho " + username + '! Adivinaste mi numero en ' + intentos + ' intentos')
if adivinar != number:
    number = str(number)
    print("Lo siento " + username + ' el numero que yo pensaba era el: ' + number)