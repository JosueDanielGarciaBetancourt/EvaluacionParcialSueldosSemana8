import unittest
from src.logica.CalculoSueldo import CalcularSueldo


class Prueba_Sueldos(unittest.TestCase):
    def setUp(self):
        self.calculoSueldo = CalcularSueldo(150.00, 1, 1, 1, 1000, 0.03)

    def tearDown(self):
        self.calculoSueldo = None
        self.calculoSueldo2 = None

    def test_TodosLosParametrosCorrectos_retornaSueldoNeto(self):
        # Arrange
        sueldoNetoManual = 1116.87

        # Do
        SueldoNetoCalculado = self.calculoSueldo.CalcularSueldoNeto()

        # Assert
        self.assertAlmostEqual(SueldoNetoCalculado, sueldoNetoManual, places=2)

    def test_ParametrosVacios_retornaExcepcion(self):
        with self.assertRaises(ValueError):
            self.calculoSueldo2 = CalcularSueldo(None, None, None, None, None, None)


    """def test_TresCoeficientesNoNumericos_lanzaException(self):
        # Act y Assert
        with self.assertRaises(ExceptionDatos):
            self.ecuacionSegundoGrado.coeficientes = ["a", "b", "c"]

    def test_RaicesComplejas_retornaRaicesComplejas(self):
        # Arrange
        self.ecuacionSegundoGrado.coeficientes = [1, 0, 1]
        raiz1 = complex(0, 1)
        raiz2 = complex(0, -1)

        # Do
        raiz1Calculada, raiz2Calculada = self.ecuacionSegundoGrado.calcular_raices()

        # Assert
        self.assertEqual(raiz1Calculada, raiz1)
        self.assertEqual(raiz2Calculada, raiz2)

    def test_RaicesCero_retornaRaicesReales(self):
        # Arrange
        self.ecuacionSegundoGrado.coeficientes = [1, 4, 0]
        raiz1 = 0.00
        raiz2 = -4.00

        # Do
        raiz1Calculada, raiz2Calculada = self.ecuacionSegundoGrado.calcular_raices()

        # Assert
        self.assertEqual(raiz1Calculada, raiz1)
        self.assertEqual(raiz2Calculada, raiz2)
"""