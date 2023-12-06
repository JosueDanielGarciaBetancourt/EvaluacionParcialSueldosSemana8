from src.modelo.conexion_db import Conexion
from tkinter import messagebox

class SQLBoletaPago:
    def __init__(self, id_boleta=None, sueldo_neto=None, descuento_total=None, bonificacion_total=None, fecha_emision=None, id_empleado=None):
        self.id_boleta = id_boleta
        self.sueldo_neto = sueldo_neto
        self.descuento_total = descuento_total
        self.bonificacion_total = bonificacion_total
        self.fecha_emision = fecha_emision
        self.id_empleado = id_empleado

        self.conexion = Conexion()
        self.cursor = self.conexion.cursor()

    def AgregarBoletaPago(self):
        dato = (self.id_boleta, self.sueldo_neto, self.descuento_total, self.bonificacion_total, self.fecha_emision, self.id_empleado)
        consulta = "INSERT INTO tblBoletaPago (IDBoleta, bolSueldoNeto, bolDescuentoTotal, bolBonificacionTotal, bolFechaEmision, IDEmpleado) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            messagebox.showinfo('Mensaje', 'Boleta de pago agregada correctamente')
        except Exception as e:
            messagebox.showinfo('Mensaje de error', f'Error al agregar boleta de pago: {e}')
        finally:
            self.CerrarConexion()

    def LeerBoletaPago(self):
        lista = []
        dato = (self.id_boleta,)
        consulta = "SELECT * FROM tblBoletaPago WHERE IDBoleta=?"
        try:
            self.cursor.execute(consulta, dato)
            resultado = self.cursor.fetchone()
            if resultado:
                lista = resultado
            else:
                mensaje = "Boleta de pago no encontrada."
                return mensaje
        except Exception as e:
            print(f'Error al leer boleta de pago: {e}')
        finally:
            self.CerrarConexion()

        return lista

    def ObtenerUltimoCodigo(self):
        consulta = "SELECT TOP 1 IDBoleta FROM tblBoletaPago ORDER BY IDBoleta DESC"
        try:
            self.cursor.execute(consulta)
            ultimo_codigo = self.cursor.fetchone()
            if ultimo_codigo:
                return str(ultimo_codigo[0])
            else:
                return None  # Retorna None si no hay boletas de pago en la base de datos
        except Exception as e:
            print(f'Error al obtener el último código de boleta de pago: {e}')
        finally:
            self.CerrarConexion()

    def CerrarConexion(self):
        try:
            self.cursor.close()
            self.conexion.close()
        except Exception as e:
            print(f'Error al cerrar la conexión: {e}')