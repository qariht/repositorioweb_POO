"""Interfaz de consola para demostrar el modelo orientado a objetos."""

from .curso import Curso
from .recurso import Recurso
from .usuario import Administrador, Estudiante


class AplicacionConsola:
    """Coordina las opciones del menú sin mezclarlo con las clases del dominio."""

    def __init__(self, repositorio, entrada=input, salida=print):
        self.repositorio = repositorio
        self.entrada = entrada
        self.salida = salida

    def cargar_datos_iniciales(self):
        """Añade datos mínimos para que el proyecto pueda demostrarse al ejecutarlo."""
        if not self.repositorio.buscar_curso("IS-282"):
            self.repositorio.registrar_curso(Curso("IS-282", "Programación Orientada a Objetos"))

        if not self.repositorio.buscar_usuario("ADM001"):
            administrador = Administrador(
                "ADM001",
                "ADM001",
                "admin@unsch.edu.pe",
                "clave-admin",
            )
            self.repositorio.registrar_usuario(administrador)

    def iniciar(self):
        self.cargar_datos_iniciales()
        self.salida(f"\n=== {self.repositorio.nombre} ===")
        self.salida("Avance 2: gestión interactiva por consola.")

        opcion = ""
        while opcion != "4":
            self._mostrar_menu_principal()
            opcion = self.entrada("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                self.mostrar_recursos(self.repositorio.recursos)
            elif opcion == "4":
                self.salida("Gracias por usar el repositorio académico.")
            else:
                self.salida("Opción no válida.")

    def _mostrar_menu_principal(self):
        self.salida("\n1. Registrar estudiante")
        self.salida("2. Iniciar sesión")
        self.salida("3. Ver recursos publicados")
        self.salida("4. Salir")

    def registrar_estudiante(self):
        self.salida("\n--- Registro de estudiante ---")
        codigo = self.entrada("Código de estudiante: ").strip()
        correo = self.entrada("Correo institucional: ").strip()
        contrasena = self.entrada("Contraseña: ").strip()
        semestre = self._leer_entero("Semestre actual: ")

        if not codigo or not contrasena or semestre is None:
            self.salida("Registro cancelado: complete los datos correctamente.")
            return

        estudiante = Estudiante(f"EST-{codigo}", codigo, correo, contrasena, semestre)
        if self.repositorio.registrar_usuario(estudiante):
            self.salida("Estudiante registrado correctamente.")
            self.salida(f"Su identificador de inicio de sesión es: {estudiante.usuario_id}")
        else:
            self.salida("No se pudo registrar. Use correo @unsch.edu.pe y un código no registrado.")

    def iniciar_sesion(self):
        self.salida("\n--- Inicio de sesión ---")
        usuario_id = self.entrada("Identificador de usuario: ").strip()
        contrasena = self.entrada("Contraseña: ").strip()
        usuario = self.repositorio.autenticar_usuario(usuario_id, contrasena)

        if not usuario:
            self.salida("Credenciales inválidas o usuario bloqueado.")
            return

        self.salida(f"Bienvenido/a, {usuario.nombre_completo}. Rol: {usuario.obtener_rol()}")
        if isinstance(usuario, Estudiante):
            self.menu_estudiante(usuario)
        elif isinstance(usuario, Administrador):
            self.menu_administrador(usuario)

    def menu_estudiante(self, estudiante):
        opcion = ""
        while opcion != "4":
            self.salida("\n--- Menú de estudiante ---")
            self.salida("1. Publicar recurso")
            self.salida("2. Buscar recursos")
            self.salida("3. Ver mis recursos")
            self.salida("4. Cerrar sesión")
            opcion = self.entrada("Seleccione una opción: ").strip()

            if opcion == "1":
                self.publicar_recurso(estudiante)
            elif opcion == "2":
                self.buscar_recursos()
            elif opcion == "3":
                self.mostrar_recursos(estudiante.recursos_publicados)
            elif opcion != "4":
                self.salida("Opción no válida.")

    def menu_administrador(self, administrador):
        opcion = ""
        while opcion != "5":
            self.salida("\n--- Menú de administrador ---")
            self.salida("1. Registrar curso")
            self.salida("2. Ver usuarios")
            self.salida("3. Bloquear usuario")
            self.salida("4. Ver recursos publicados")
            self.salida("5. Cerrar sesión")
            opcion = self.entrada("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_curso()
            elif opcion == "2":
                self.mostrar_usuarios()
            elif opcion == "3":
                self.bloquear_usuario(administrador)
            elif opcion == "4":
                self.mostrar_recursos(self.repositorio.recursos)
            elif opcion != "5":
                self.salida("Opción no válida.")

    def registrar_curso(self):
        self.salida("\n--- Registro de curso ---")
        codigo = self.entrada("Código del curso: ").strip()
        nombre = self.entrada("Nombre del curso: ").strip()

        if codigo and nombre and self.repositorio.registrar_curso(Curso(codigo, nombre)):
            self.salida("Curso registrado correctamente.")
        else:
            self.salida("No se pudo registrar el curso. Verifique que el código no esté repetido.")

    def bloquear_usuario(self, administrador):
        usuario_id = self.entrada("Identificador del usuario que desea bloquear: ").strip()
        usuario = self.repositorio.buscar_usuario(usuario_id)

        if not usuario:
            self.salida("Usuario no encontrado.")
        elif usuario is administrador:
            self.salida("El administrador no puede bloquear su propia cuenta.")
        else:
            administrador.bloquear_usuario(usuario)
            self.salida(f"Usuario {usuario.usuario_id} bloqueado correctamente.")

    def publicar_recurso(self, estudiante):
        self.salida("\n--- Publicación de recurso ---")
        titulo = self.entrada("Título: ").strip()
        descripcion = self.entrada("Descripción: ").strip()
        codigo_curso = self.entrada("Código de curso: ").strip()
        curso = self.repositorio.buscar_curso(codigo_curso)

        if not curso:
            self.salida("El curso no está registrado. Consulte al administrador.")
            return

        self.salida("Tipo de aporte: 1. Código | 2. Reporte | 3. Examen")
        tipo_aporte = self._leer_tipo_aporte()
        nombre_archivo = self.entrada("Nombre del archivo: ").strip()
        tamanio_mb = self._leer_decimal("Tamaño del archivo en MB: ")

        if not titulo or not descripcion or not tipo_aporte or tamanio_mb is None:
            self.salida("Publicación cancelada: complete los datos correctamente.")
            return

        recurso_id = f"REC-{len(self.repositorio.recursos) + 1:03d}"
        recurso = Recurso(
            recurso_id,
            titulo,
            descripcion,
            estudiante,
            curso,
            tipo_aporte,
            nombre_archivo,
            tamanio_mb,
        )

        if self.repositorio.publicar_recurso(recurso):
            self.salida("Recurso publicado correctamente.")
        else:
            extensiones = ", ".join(Recurso.EXTENSIONES_PERMITIDAS)
            self.salida(f"No se pudo publicar. Formatos: {extensiones}; tamaño máximo: 20 MB.")

    def buscar_recursos(self):
        texto = self.entrada("Palabra clave (deje vacío para todos): ").strip()
        codigo_curso = self.entrada("Código de curso (deje vacío para todos): ").strip()
        resultados = self.repositorio.buscar_recursos(texto, codigo_curso or None)
        self.mostrar_recursos(resultados)

    def mostrar_recursos(self, recursos):
        if not recursos:
            self.salida("No hay recursos para mostrar.")
            return

        self.salida("\n--- Recursos publicados ---")
        for recurso in recursos:
            self.salida(
                f"[{recurso.recurso_id}] {recurso.titulo} | {recurso.curso.codigo} | "
                f"{recurso.tipo_aporte} | {recurso.nombre_archivo} | {recurso.tamanio_mb} MB"
            )

    def mostrar_usuarios(self):
        self.salida("\n--- Usuarios registrados ---")
        for usuario in self.repositorio.usuarios:
            estado = "Activo" if usuario.activo else "Bloqueado"
            self.salida(f"{usuario.usuario_id} | {usuario.obtener_rol()} | {usuario.correo} | {estado}")

    def _leer_entero(self, mensaje):
        valor = self.entrada(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        return None

    def _leer_decimal(self, mensaje):
        valor = self.entrada(mensaje).strip().replace(",", ".")
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        return None

    def _leer_tipo_aporte(self):
        opciones = {"1": "Código", "2": "Reporte", "3": "Examen"}
        return opciones.get(self.entrada("Seleccione el tipo: ").strip())
