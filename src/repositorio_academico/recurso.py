"""Clase que representa un material publicado en el repositorio."""


class Recurso:
    EXTENSIONES_PERMITIDAS = (".py", ".tex", ".pdf", ".zip")
    TAMANIO_MAXIMO_MB = 20
    TIPOS_APORTE = ("Código", "Reporte", "Examen")

    def __init__(
        self,
        recurso_id,
        titulo,
        descripcion,
        autor,
        curso,
        tipo_aporte,
        nombre_archivo,
        tamanio_mb,
    ):
        self.recurso_id = recurso_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.autor = autor
        self.curso = curso
        self.tipo_aporte = tipo_aporte
        self.nombre_archivo = nombre_archivo
        self.tamanio_mb = tamanio_mb
        self._publicado = False

    @property
    def publicado(self):
        return self._publicado

    def tiene_formato_permitido(self):
        return self.nombre_archivo.lower().endswith(self.EXTENSIONES_PERMITIDAS)

    def tiene_tamanio_permitido(self):
        return 0 < self.tamanio_mb <= self.TAMANIO_MAXIMO_MB

    def tiene_tipo_valido(self):
        return self.tipo_aporte in self.TIPOS_APORTE

    def puede_publicarse(self):
        return (
            self.autor.activo
            and self.curso.activo
            and self.tiene_formato_permitido()
            and self.tiene_tamanio_permitido()
            and self.tiene_tipo_valido()
        )

    def publicar(self):
        if self.puede_publicarse():
            self._publicado = True
            return True
        return False
