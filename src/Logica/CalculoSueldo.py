class CalcularSueldo:
    def __init__(self, sueldo, horasExtra, diasFalta, minutosTardanza, Movilidad, Suplementaria):
        if any(param is None for param in [sueldo, horasExtra, diasFalta, minutosTardanza, Movilidad, Suplementaria]):
            raise ValueError("Ningún parámetro puede ser None")

        self.horasExtra = horasExtra
        self.sueldo = sueldo
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.Movilidad = Movilidad
        self.Suplementaria = Suplementaria

    def CalculoBonificaciones(self):
        self.PagoHorasExtra = 1.50 * self.horasExtra * ((self.sueldo / 30) / 8)
        self.BonificacionSumplementaria = self.Suplementaria * self.sueldo
        self.Bonificaciones = self.Movilidad + self.BonificacionSumplementaria + self.PagoHorasExtra
        self.remuneracionComputable = self.sueldo + self.Movilidad + self.BonificacionSumplementaria
        return self.Bonificaciones

    def CalculoDescuentos(self):
        self.remuneracionMinima = self.sueldo + self.Bonificaciones
        self.DescuentoFaltas = self.remuneracionComputable / 30 * self.diasFalta
        self.DescuentoTardanza = (((self.remuneracionComputable / 30) / 8) / 60) * self.minutosTardanza
        self.descuentos = self.DescuentoFaltas + self.DescuentoTardanza
        return self.descuentos

    def CalcularSueldoNeto(self):
        sueldoBasico = self.sueldo
        bonificaciones = self.CalculoBonificaciones()
        descuentos = self.CalculoDescuentos()
        sueldoNeto = sueldoBasico + bonificaciones - descuentos
        sueldoNeto = round(sueldoNeto, 2)

        """"# Imprimir atributos
        print(f"sueldo: {self.sueldo}")
        print(f"horasExtra: {self.horasExtra}")
        print(f"diasFalta: {self.diasFalta}")
        print(f"minutosTardanza: {self.minutosTardanza}")
        print(f"Movilidad: {self.Movilidad}")
        print(f"Suplementaria: {self.Suplementaria}")
        print(f"PagoHorasExtra: {self.PagoHorasExtra}")

        # Imprimir otros atributos si es necesario
        print(f"BonificacionSumplementaria: {self.BonificacionSumplementaria}")
        print(f"Bonificaciones: {self.Bonificaciones}")
        print(f"remuneracionComputable: {self.remuneracionComputable}")
        print(f"remuneracionMinima: {self.remuneracionMinima}")
        print(f"DescuentoFaltas: {self.DescuentoFaltas}")
        print(f"DescuentoTardanza: {self.DescuentoTardanza}")
        print(f"descuentos: {self.descuentos}")
        print(f"SUELDO NETO: {sueldoNeto}")"""
        return sueldoNeto

