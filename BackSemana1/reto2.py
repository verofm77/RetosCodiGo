import datetime
#VARIABLES
personas = []

def ConvertirFechaEnDias(strFecha):
    resultado = (datetime.datetime.now() - datetime.datetime.fromisoformat(strFecha)).days
    return resultado 
#ENTRADAS
nroPersonas = int(input("Cantidad de Personas a ingresar: "))
for c in range(nroPersonas):
    nombre = input("Nombre: ")
    dni = input("DNI:")
    fechanac = input("Fecha Nacimiento(AÑO-MES-DIA): ")
    persona = [
        ConvertirFechaEnDias(fechanac) ,
        {
        'nombre': nombre,
        'dni': dni,
        'fechanac': fechanac
        }
    ]
    personas.append(persona)

#PROCESO
personas.sort()

#SALIDAS
for a in personas:
    print(a)