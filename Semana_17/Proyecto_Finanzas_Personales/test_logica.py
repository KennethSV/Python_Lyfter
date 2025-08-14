
import os
import tempfile
import unittest
from pathlib import Path
import persistencia
from logica import GestorFinanzas, Categoria, Movimiento

class TestLogicaFinanzas(unittest.TestCase):

    def setUp(self):
        # Cada prueba trabaja en un directorio temporal separado
        self.tmpdir = tempfile.TemporaryDirectory()
        self.data_dir = self.tmpdir.name
        self.gestor = GestorFinanzas(self.data_dir)

    def tearDown(self):
        self.tmpdir.cleanup()

    # 1: carga inicial vacía
    def test_carga_inicial_vacia(self):
        self.assertEqual(self.gestor.listar_categorias(), [])
        self.assertEqual(self.gestor.listar_movimientos(), [])

    # 2: agregar categoría válida
    def test_agregar_categoria_valida(self):
        self.gestor.agregar_categoria("Comida")
        self.assertIn("Comida", self.gestor.listar_categorias())

    # 3: evitar categorías duplicadas (case-insensitive)
    def test_categoria_duplicada(self):
        self.gestor.agregar_categoria("Transporte")
        with self.assertRaises(ValueError):
            self.gestor.agregar_categoria(" transporte ")  # mismo nombre con espacios

    # 4: no permitir movimientos sin categorías
    def test_movimiento_sin_categorias(self):
        with self.assertRaises(RuntimeError):
            self.gestor.agregar_gasto("Almuerzo", 3500, "Comida")

    # 5: validar monto positivo
    def test_monto_invalido(self):
        self.gestor.agregar_categoria("Varios")
        with self.assertRaises(ValueError):
            self.gestor.agregar_ingreso("Error", 0, "Varios")
        with self.assertRaises(ValueError):
            self.gestor.agregar_ingreso("Error", -10, "Varios")

    # 6: validar título no vacío
    def test_titulo_vacio(self):
        self.gestor.agregar_categoria("Hogar")
        with self.assertRaises(ValueError):
            self.gestor.agregar_gasto("", 1000, "Hogar")

    # 7: persistencia al guardar y recargar
    def test_persistencia(self):
        self.gestor.agregar_categoria("Salud")
        self.gestor.agregar_ingreso("Pago", 10000, "Salud")
        self.gestor.agregar_gasto("Medicina", 2500, "Salud")
        # Nuevo gestor en el mismo directorio
        gestor2 = GestorFinanzas(self.data_dir)
        self.assertIn("Salud", gestor2.listar_categorias())
        movs = gestor2.listar_movimientos()
        self.assertEqual(len(movs), 2)
        # Balance debería coincidir
        self.assertEqual(gestor2.balance(), 7500.00)

    # 8: balance con múltiples movimientos
    def test_balance_varios(self):
        self.gestor.agregar_categoria("Trabajo")
        self.gestor.agregar_ingreso("Salario", 5000, "Trabajo")
        self.gestor.agregar_gasto("Almuerzo", 1500, "Trabajo")
        self.gestor.agregar_gasto("Taxi", 800, "Trabajo")
        self.assertEqual(self.gestor.balance(), 2700.00)

    # 9: categoría inexistente al agregar movimiento
    def test_categoria_inexistente(self):
        self.gestor.agregar_categoria("Casa")
        with self.assertRaises(ValueError):
            self.gestor.agregar_gasto("Silla", 100, "Hogar")

    # 10: tipos de movimiento válidos
    def test_tipo_movimiento(self):
        self.gestor.agregar_categoria("Entretenimiento")
        self.gestor.agregar_ingreso("Reembolso", 200, "Entretenimiento")
        self.gestor.agregar_gasto("Película", 50, "Entretenimiento")
        tipos = {m["tipo"] for m in self.gestor.listar_movimientos()}
        self.assertEqual(tipos, {"ingreso", "gasto"})

if __name__ == "__main__":
    unittest.main(verbosity=2)
