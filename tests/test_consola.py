"""Pruebas de las acciones principales del menú de consola."""

import unittest

from src.repositorio_academico import AplicacionConsola, RepositorioAcademico


class PruebasDeConsola(unittest.TestCase):
    def crear_consola(self, respuestas):
        valores = iter(respuestas)
        mensajes = []
        consola = AplicacionConsola(
            RepositorioAcademico("Repositorio de prueba"),
            entrada=lambda _mensaje: next(valores),
            salida=mensajes.append,
        )
        return consola, mensajes

    def test_carga_curso_y_administrador_para_la_demostracion(self):
        consola, _ = self.crear_consola([])
        consola.cargar_datos_iniciales()

        self.assertIsNotNone(consola.repositorio.buscar_curso("IS-282"))
        self.assertIsNotNone(consola.repositorio.buscar_usuario("ADM001"))

    def test_registra_estudiante_desde_el_menu(self):
        consola, mensajes = self.crear_consola(
            ["20251001", "ana@unsch.edu.pe", "clave", "4"]
        )
        consola.registrar_estudiante()

        estudiante = consola.repositorio.buscar_usuario("EST-20251001")
        self.assertIsNotNone(estudiante)
        self.assertTrue(estudiante.autenticar("clave"))
        self.assertIn("Estudiante registrado correctamente.", mensajes)


if __name__ == "__main__":
    unittest.main()
