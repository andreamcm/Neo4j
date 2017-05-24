class Doctores(GraphObject):
    __primarykey__ = "nombre"

    nombre = Property()
    edad = Property()
    especialidad = Property()
    telefono = Property()
    colegiado = Property()

    revisa_a = RelatedTo (Doctores)

