import subprocess
from src.logica.ClaseEmpleado import SQLEmpleado
from src.logica.ClaseBoletaPago import SQLBoletaPago
from fpdf import FPDF

class GeneradorBoletaPago(FPDF):
    def __init__(self, id_boleta, id_empleado):
        super().__init__()
        self.id_boleta = id_boleta
        self.id_empleado=id_empleado
        self.generar_boleta()

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Boleta de Pago', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def generar_boleta(self):
        # Obtener datos del empleado y boleta
        empleado = SQLEmpleado(id=self.id_empleado)
        datos_empleado = empleado.LeerEmpleado()
        nombre = datos_empleado[0][1]
        sueldo_basico = datos_empleado[0][2]
        cargo = datos_empleado[0][3]

        boleta = SQLBoletaPago(self.id_boleta)
        datos_boleta = boleta.LeerBoletaPago()
        sueldo_neto = datos_boleta[1]
        descuento = datos_boleta[2]
        bonificacion = datos_boleta[3]
        fecha_emision = datos_boleta[4]

        # Agregar detalles a la boleta
        self.add_page()
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'ID Empleado: {}'.format(self.id_empleado), 0, 1)
        self.cell(0, 10, 'Nombre del Empleado: {}'.format(nombre), 0, 1)
        self.cell(0, 10, 'Cargo: {}'.format(cargo), 0, 1)
        self.cell(0, 10, 'Sueldo básico: {}'.format(sueldo_basico), 0, 1)
        self.cell(0, 10, 'ID Boleta: {}'.format(self.id_boleta), 0, 1)
        self.cell(0, 10, f'Fecha de emisión: {fecha_emision}')
        self.ln(10)

        # Encabezados de la tabla
        self.set_fill_color(200, 220, 255)
        self.cell(40, 10, 'Concepto', 1, 0, 'C', 1)
        self.cell(40, 10, 'Monto', 1, 1, 'C', 1)

        # Contenido de la tabla
        self.cell(40, 10, 'Descuento Total', 1)
        self.cell(40, 10, '${:.2f}'.format(float(descuento)), 1, 1)
        self.cell(40, 10, 'Bonificación Total', 1)
        self.cell(40, 10, '${:.2f}'.format(float(bonificacion)), 1, 1)
        self.cell(40, 10, 'Sueldo Neto', 1)
        self.cell(40, 10, '${:.2f}'.format(float(sueldo_neto)), 1, 1)

        # Calcular la posición y para centrar la tabla verticalmente
        y_position = (self.h - self.get_y()) / 2
        self.set_y(y_position)

        # Calcular la posición x para centrar la tabla horizontalmente
        x_position = (self.w - 80) / 2
        self.set_x(x_position)

        # Guardar el PDF en un archivo
        nombre_archivo = f'src/modelo/BoletasDePago/boleta_pago_{self.id_boleta}.pdf'
        self.output(nombre_archivo)

        # Abrir el archivo PDF
        subprocess.run(["start", "", nombre_archivo], shell=True, check=True)

