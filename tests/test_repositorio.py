"""Pruebas del avance inicial."""

import unittest

from src.repositorio_academico import Administrador, Curso, Estudiante, Recurso, RepositorioAcademico, Usuario


class PruebasDeUsuarios(unittest.TestCase):
    def setUp(self):
        self.estudiante = Estudiante("U001", "20251001", "ana@unsch.edu.pe", "secreta", 4)

    def test_estudiante_hereda_de_usuario(self):
        self.assertIsInstance(self.estudiante, Usuario)
        self.assertEqual(self.estudiante.obtener_rol(), "Estudiante")

    def test_autenticacion_y_correo_institucional(self):
        self.assertTrue(self.estudiante.tiene_correo_institucional())
        self.assertTrue(self.estudiante.autenticar("secreta"))
        self.assertFalse(self.estudiante.autenticar("incorrecta"))

    def test_repositorio_autentica_usuario_registrado(self):
        repositorio = RepositorioAcademico("Repositorio de prueba")
        repositorio.registrar_usuario(self.estudiante)

        self.assertIs(repositorio.autenticar_usuario("U001", "secreta"), self.estudiante)
        self.assertIsNone(repositorio.autenticar_usuario("U001", "incorrecta"))

    def test_administrador_puede_bloquear_usuario(self):
        administrador = Administrador("A001", "ADM01", "admin@unsch.edu.pe", "clave")
        administrador.bloquear_usuario(self.estudiante)
        self.assertFalse(self.estudiante.activo)
        self.assertFalse(self.estudiante.autenticar("secreta"))


class PruebasDeRecursos(unittest.TestCase):
    def setUp(self):
        self.repositorio = RepositorioAcademico("Repositorio de prueba")
        self.curso = Curso("IS-282", "Programación Orientada a Objetos")
        self.estudiante = Estudiante("U001", "20251001", "ana@unsch.edu.pe", "secreta", 4)
        self.repositorio.registrar_curso(self.curso)
        self.repositorio.registrar_usuario(self.estudiante)

    def crear_recurso(self, nombre_archivo="herencia.py", tamanio_mb=1):
        return Recurso(
            "R001",
            "Guía de herencia",
            "Ejemplo básico de herencia simple.",
            self.estudiante,
            self.curso,
            "Código",
            nombre_archivo,
            tamanio_mb,
        )

    def test_publica_recurso_valido_y_lo_encuentra(self):
        recurso = self.crear_recurso()
        self.assertTrue(self.repositorio.publicar_recurso(recurso))
        self.assertTrue(recurso.publicado)
        self.assertEqual(self.repositorio.buscar_recursos("herencia"), [recurso])
        self.assertEqual(self.estudiante.recursos_publicados, (recurso,))

    def test_no_publica_archivo_con_formato_o_tamanio_invalido(self):
        archivo_no_permitido = self.crear_recurso("notas.docx")
        archivo_grande = self.crear_recurso("material.pdf", 20.1)

        self.assertFalse(self.repositorio.publicar_recurso(archivo_no_permitido))
        self.assertFalse(self.repositorio.publicar_recurso(archivo_grande))

    def test_no_registra_correo_externo(self):
        externo = Estudiante("U002", "20251002", "externo@gmail.com", "clave", 4)
        self.assertFalse(self.repositorio.registrar_usuario(externo))

    def test_busca_recursos_por_curso(self):
        recurso = self.crear_recurso("poo.pdf")
        self.repositorio.publicar_recurso(recurso)

        self.assertEqual(self.repositorio.buscar_recursos(codigo_curso="IS-282"), [recurso])
        self.assertEqual(self.repositorio.buscar_recursos(codigo_curso="IS-999"), [])


if __name__ == "__main__":
    unittest.main()
