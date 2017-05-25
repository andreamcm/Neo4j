class Personas(GraphObject):
    __primarykey__ = "nombre"

    nombre = Property()

    conoce_a = RelatedTo (Personas)

    
