# Universidad del Valle de Guatemala
# Algoritmos y Estructura de Datos
# Grupo 2

from Hospital import *

print "Bienvenid@ al Hospital Neo4j"
print "Este programa le permitira anadir pacientes, doctores,\n consultas y recomendar ciertos doctores a sus conocidos."
print "Para comenzar a usar este servicio seleccione una de las siguientes opciones: \n"

trabajar = True

while (trabajar == True):
    print "1. Ingresar un paciente"
    print "2. Ingresar un doctor"
    print "3. Ingresar una cita medica"
    print "4. Encontrar a un doctor por su especialidad"
    print "5. Contactar a un doctor debido a un conocido"
    print "6. Salir del Hospital"

    seleccion = int(raw_input("¿Que opcion desea realizar?: "))

    if seleccion == 1:
        nombre = raw_input("Nombre: ")
        dpi = long(raw_input("DPI: "))
        telefono = long(raw_input("Telefono: "))
        enfermedad = raw_input("Enfermedad: ")
        pacienteNuevo(nombre, dpi, telefono, enfermedad)

    if seleccion == 2:
        nombre = raw_input("Nombre: ")
        especialidad = long(raw_input("Especialidad: "))
        telefono = long(raw_input("Telefono: "))
        doctorNuevo(nombre, especialidad, telefono)

    if seleccion == 3:
        nombrePaciente = raw_input("Nombre del paciente: ")
        nombreDoctor = raw_input("Nombre del doctor: ")
        receta = raw_input("Que receto el doctor: ")
        fecha = raw_input("Fecha de la consulta: ")
        citaMedica(nombrePaciente, nombreDoctor, receta, fecha)

    if seleccion == 4:
        especialidad = raw_input("Ingrese la especialidad del doctor que busca: ")
        especialidadDoctor(especialidad)

    if seleccion == 5:
        paciente = raw_input("Ingrese el nombre del paciente que conoce al doctor: ")
        persona = raw_input("Ingrese el nombre de la persona que busca al doctor: ")
        contactos(paciente, persona)

    if seleccion == 6:
        salir()

    salir = raw_input("¿Desea salir del programa? (S/N)")

    if salir == "S":
        trabajar == False
        salir()
        print "Gracias por utilizar el Hospital Neo4j"
    else:
        trabajar == True
