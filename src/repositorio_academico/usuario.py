"""Clases de usuario del sistema."""

import hashlib


class Usuario:
    """Clase base para todas las personas que acceden al repositorio."""

    DOMINIO_INSTITUCIONAL = "@unsch.edu.pe"

    def __init__(self, usuario_id, nombre_completo, correo, contrasena):
        self.usuario_id = usuario_id
        self.nombre_completo = nombre_completo
        self._correo = correo.strip().lower()
        self.__contrasena_hash = self._generar_hash(contrasena)
        self._activo = True

    @staticmethod
    def _generar_hash(contrasena):
        return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()

    @property
    def correo(self):
        return self._correo

    @property
    def activo(self):
        return self._activo

    def tiene_correo_institucional(self):
        return self._correo.endswith(self.DOMINIO_INSTITUCIONAL)

    def autenticar(self, contrasena):
        """Comprueba la clave sin exponer su valor original."""
        return self._activo and self.__contrasena_hash == self._generar_hash(contrasena)

    def bloquear(self):
        self._activo = False

    def obtener_rol(self):
        return "Usuario"


class Estudiante(Usuario):
    """Usuario que puede publicar recursos académicos."""

    def __init__(self, usuario_id, codigo_estudiante, correo, contrasena, semestre):
        super().__init__(usuario_id, f"Estudiante {codigo_estudiante}", correo, contrasena)
        self.codigo_estudiante = codigo_estudiante
        self.semestre = semestre
        self._cursos_aprobados = []
        self._recursos_publicados = []

    @property
    def cursos_aprobados(self):
        return tuple(self._cursos_aprobados)

    @property
    def recursos_publicados(self):
        return tuple(self._recursos_publicados)

    def agregar_curso_aprobado(self, codigo_curso):
        if codigo_curso not in self._cursos_aprobados:
            self._cursos_aprobados.append(codigo_curso)
            return True
        return False

    def registrar_recurso(self, recurso):
        self._recursos_publicados.append(recurso)

    def obtener_rol(self):
        return "Estudiante"


class Administrador(Usuario):
    """Usuario responsable de acciones administrativas iniciales."""

    def __init__(self, usuario_id, codigo_administrador, correo, contrasena):
        super().__init__(usuario_id, f"Administrador {codigo_administrador}", correo, contrasena)
        self.codigo_administrador = codigo_administrador

    def bloquear_usuario(self, usuario):
        usuario.bloquear()

    def obtener_rol(self):
        return "Administrador"
