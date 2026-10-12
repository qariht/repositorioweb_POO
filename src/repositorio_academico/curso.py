"""Clase que representa un curso de la malla curricular."""


class Curso:
    def __init__(self, codigo, nombre, activo=True):
        self.codigo = codigo.upper()
        self.nombre = nombre
        self.activo = activo

    def desactivar(self):
        self.activo = False

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
