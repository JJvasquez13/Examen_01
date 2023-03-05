class Libro:
    def __init__(self, titulo, autores, editorial, fecha_publicacion, descripcion):
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion

    def __str__(self):
        autores_str = ", ".join(self.autores)
        return f"{self.titulo} de {autores_str}, publicado por {self.editorial} en {self.fecha_publicacion}. Descripción: {self.descripcion}"

    def __setattr__(self, name: str, value: any):
        super(Libro, self).__setattr__(name, value)
        
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre}, {self.nacionalidad}"

    def __setattr__(self, name: str, value: any):
        super(Autor, self).__setattr__(name, value)

class Editorial:
    def __init__(self, nombre, ciudad, estado, pais, website):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais
        self.website = website

    def __str__(self):
        return f"{self.nombre}, {self.ciudad}, {self.estado}, {self.pais}. Sitio web: {self.website}"

    def __setattr__(self, name: str, value: any):
        super(Autor, self).__setattr__(name, value)


class Persona:
    def __init__(self, identificacion, nombre_completo, tipo):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.tipo = tipo

    def __str__(self):
        return f"{self.identificacion}, {self.nombre_completo}, {self.tipo}"

    def __setattr__(self, name: str, value: any):
        super(Autor, self).__setattr__(name, value)


