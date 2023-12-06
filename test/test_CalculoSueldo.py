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

    def test_calculo_bonificaciones(self):
        bonificaciones_esperadas = 1005.44
        bonificaciones = self.calculoSueldo.CalculoBonificaciones()
        self.assertAlmostEqual(bonificaciones, bonificaciones_esperadas, places=2)

    def test_calculo_descuentos(self):
        descuentos_esperados = 38.56
        self.calculoSueldo.CalculoBonificaciones()
        descuentos = self.calculoSueldo.CalculoDescuentos()
        self.assertAlmostEqual(descuentos, descuentos_esperados, places=2)

    def test_valores_no_numericos(self):
        with self.assertRaises(ValueError):
            CalcularSueldo("a", "b", "c", "d", "e", "f")

    def test_parametro_nulo(self):
        with self.assertRaises(ValueError):
            CalcularSueldo(150.0, None, 1, 1, 1000, 0.03)

    def test_SueldoNetos(self):
        # Arrange
        CalcularSueldo2 = CalcularSueldo(150.0, 1, 1, 1, 1000, 0.03)
        items = (
            {"CalculoSueldo_N": "1","SueldoBase": 150.00, "HorasExtra": 1, "DiasFalta": 1, "MinutosTardanza": 1,
             "Movilidad": 1000,"Suplementaria": 0.03,"SueldoNeto": 1116.87},
            {"CalculoSueldo_N": "2", "SueldoBase": 500.00, "HorasExtra": 4, "DiasFalta": 5, "MinutosTardanza": 7,
             "Movilidad": 1000,"Suplementaria": 0.03,"SueldoNeto": 1274.26},
            {"CalculoSueldo_N": "3", "SueldoBase": 1000.00, "HorasExtra": 5, "DiasFalta": 3, "MinutosTardanza": 10,
             "Movilidad": 1000,"Suplementaria": 0.03,"SueldoNeto": 1856.84},
            {"CalculoSueldo_N": "4", "SueldoBase": 1500.00, "HorasExtra": 3, "DiasFalta": 2, "MinutosTardanza": 1,
             "Movilidad": 1000, "Suplementaria": 0.03, "SueldoNeto": 2403.28},
            {"CalculoSueldo_N": "5", "SueldoBase": 700.00, "HorasExtra": 5, "DiasFalta": 5, "MinutosTardanza": 13,
             "Movilidad": 1000, "Suplementaria": 0.03, "SueldoNeto": 1454.49},
            {"CalculoSueldo_N": "6", "SueldoBase": 450.00, "HorasExtra": 10, "DiasFalta": 3, "MinutosTardanza": 4,
             "Movilidad": 1000, "Suplementaria": 0.03, "SueldoNeto": 1344.87}
        )
        for item in items:
            with self.subTest(item["CalculoSueldo_N"]):
                CalcularSueldo2.sueldo = item["SueldoBase"]
                CalcularSueldo2.horasExtra = item["HorasExtra"]
                CalcularSueldo2.diasFalta = item["DiasFalta"]
                CalcularSueldo2.minutosTardanza = item["MinutosTardanza"]
                CalcularSueldo2.Movilidad = item["Movilidad"]
                CalcularSueldo2.Suplementaria = item["Suplementaria"]
            resultadoEsperado = item["SueldoNeto"]

            # Do
            resultadoActual = CalcularSueldo2.CalcularSueldoNeto()

            # Assert
            self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=2)


