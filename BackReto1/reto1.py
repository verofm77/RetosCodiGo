from datetime import datetime

nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
hora = datetime.now().time().hour


if (edad < 18):
    print(hora)
    if (hora > 18):
        print('Debe ir a dormir')
    else:
        print('Debe hacer la tarea')
else:
    print('No está obligado a hacer nada')