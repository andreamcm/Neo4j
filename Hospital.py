# Universidad del Valle de Guatemala
# Algoritmos y Estructura de Datos
# Grupo 2

from neo4j.v1 import GraphDatabase, basic_auth

# Acceso a la base de datos, esta esta vinculada con GitHub
# Esta base de datos esta inicialmente vacía porque el objetivo que el usuario la llene a su gusto
driver = GraphDatabase.driver("http://localhost:7474/browser/", auth = basic_auth("grupo2", "contraseña"))
session = driver.session()

# Funcion para ingresar un nuevo paciente.
def pacienteNuevo(nombre, telefono, enfermedad, dpi):
    session.run("CREATE (p: Paciente {nombre: {nombre}, telefono: {telefono}, enfermedad: {enfermedad}, dpi: {dpi}})",
    {"nombre": nombre, "telefono": telefono, "enfermedad": enfermedad, "dpi": dpi})

# Funcion para ingresar un nuevo doctor.
def doctorNuevo(nombre, especialidad, telefono):
    session.run("CREATE (d: Doctor {nombre: {nombre}, telefono: {telefono}, especialidad: {especialidad}})",
    {"nombre": nombre, "telefono": telefono, "especialidad": especialidad})

# Funcion para agendar una cita con un doctor especifico.
def citaMedica(nombrePaciente, nombreDoctor, receta, fecha):
    session.run("MATCH (paciente: Paciente)-[:Consulto]->(doctor: Doctor)"
    "WHERE paciente.dpi = {dpiPaciente} and doctor.nombre = {nombreDoctor}"
    "CREATE (paciente)-[:VISITO {fecha: {fecha}}]->(doctor), (doctor)-[:RECETO{medicina: {medicina}}]->paciente",
    {"nombrePaciente": nombrePaciente, "nombreDoctor": nombreDoctor, "receta": medicina, "fecha": fecha})
    print (nombrePaciente + " visito a el doctor " + nombreDoctor + " quien le receto " + receta + " el dia " + fecha)

# Funcion para consultar qué doctores tienen cierta especialidad.
def especialidadDoctor(especialidad):
    listado = session.run("MATCH (d: Doctor) WHERE d.especialidad = {especialidad}"
    "RETURN d.nombre AS name",
    {"especialidad": especialidad})

    for lista in listado:
        print ("La especialidad: " + especialidad + " la tienen los doctores: " + lista["name"])

# Funcion para relacionar dos personas que se conocen y sus doctores.
def contactos(persona, paciente):
    session.run("MATCH (paciente: Paciente), (persona: Paciente)"
    "WHERE paciente.nombre = {paciente} AND persona.nombre = {persona}"
    "CREATE (paciente)-[:CONOCE]->(persona)",
    {"paciente": paciente, "persona": persona})

# Funcion para salir de la base de datos.
def salir():
    session.close()
