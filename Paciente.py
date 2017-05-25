class Paciente(GraphObject):
    __primarykey__ = "nombre"

    nombre = Property()
    edad = Property()
    telefono = Property()
    fecha = Property()

    doctor = RelatedFrom ("Doctores", "REVISA_A")
    persona = RelateFrom ("Personas", "CONOCE_A")

    
