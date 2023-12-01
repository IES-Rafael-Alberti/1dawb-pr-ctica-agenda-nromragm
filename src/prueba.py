contactos_datos = [
    "Laura;Iglesias;liglesias@gmail.com;666777333;666888555;607889988",
    "Antonio;Amargo;aamargo@gmail.com",
    "Marta;Copete;marcopete@gmail.com;+34600888800",
    "Rafael;Ciruelo;rciruelo@gmail.com;+34607212121;655001122",
    "Daniela;Alba;danalba@gmail.com;+34600606060;+34670898934",
    "Rogelio;Rojo;rogrojo@gmail.com;610000099;645000013"
]
def cargar_contactos(contactos_datos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...
    lista_contactos = []

    for linea in contactos_datos:
            datos = linea.split(";")
            nombre = datos[0]
            apellido = datos[1]
            email = datos[2]
            telefonos = datos[3:] if len(datos) > 3 else []

            contacto_dict = {"nombre": nombre, "apellido": apellido, "email": email, "telefonos": telefonos}
            lista_contactos.append(contacto_dict)

    for i in lista_contactos:
          print(i)
    

cargar_contactos(contactos_datos)