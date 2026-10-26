"""Clase coordinadora del avance inicial."""

from .usuario import Estudiante


class RepositorioAcademico:
    def __init__(self, nombre):
        self.nombre = nombre
        self._usuarios = []
        self._cursos = []
        self._recursos = []

    @property
    def usuarios(self):
        return tuple(self._usuarios)

    @property
    def cursos(self):
        return tuple(self._cursos)

    @property
    def recursos(self):
        return tuple(self._recursos)

    def registrar_usuario(self, usuario):
        if not usuario.tiene_correo_institucional() or self.buscar_usuario(usuario.usuario_id):
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, usuario_id):
        for usuario in self._usuarios:
            if usuario.usuario_id == usuario_id:
                return usuario
        return None

    def autenticar_usuario(self, usuario_id, contrasena):
        """Devuelve el usuario autenticado o ``None`` cuando los datos no son válidos."""
        usuario = self.buscar_usuario(usuario_id)

        if usuario and usuario.autenticar(contrasena):
            return usuario
        return None

    def registrar_curso(self, curso):
        if self.buscar_curso(curso.codigo):
            return False
        self._cursos.append(curso)
        return True

    def buscar_curso(self, codigo_curso):
        for curso in self._cursos:
            if curso.codigo == codigo_curso.upper():
                return curso
        return None

    def publicar_recurso(self, recurso):
        """Publica solo recursos de estudiantes registrados y cursos existentes."""
        autor_registrado = self.buscar_usuario(recurso.autor.usuario_id) is recurso.autor
        curso_registrado = self.buscar_curso(recurso.curso.codigo) is recurso.curso

        if not isinstance(recurso.autor, Estudiante) or not autor_registrado or not curso_registrado:
            return False

        if recurso.publicar():
            self._recursos.append(recurso)
            recurso.autor.registrar_recurso(recurso)
            return True
        return False

    def buscar_recursos(self, texto="", codigo_curso=None):
        texto = texto.lower().strip()
        resultados = []

        for recurso in self._recursos:
            coincide_texto = texto in recurso.titulo.lower() or texto in recurso.descripcion.lower()
            coincide_curso = codigo_curso is None or recurso.curso.codigo == codigo_curso.upper()

            if recurso.publicado and coincide_texto and coincide_curso:
                resultados.append(recurso)

        return resultados
