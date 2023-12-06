from src.modelo.conexion_db import Conexion
from tkinter import messagebox
class SQLDetalleMensualTrabajador:
    def __init__(self, IDEmpleado=None, IDMes=None, detailAnio=None, detailHorasExtra=None, detailMinutosTardanzas=None, detailMinutosJustificados=None, detailDiasFalta=None, detailDiasJustificados=None, detailSueldoNeto=None):
        self.IDEmpleado = IDEmpleado
        self.IDMes = IDMes
        self.detailAnio = detailAnio
        self.detailHorasExtra = detailHorasExtra
        self.detailMinutosTardanzas = detailMinutosTardanzas
        self.detailMinutosJustificados = detailMinutosJustificados
        self.detailDiasFalta = detailDiasFalta
        self.detailDiasJustificados = detailDiasJustificados
        self.detailSueldoNeto = detailSueldoNeto
        self.conexion = Conexion()
        self.cursor = self.conexion.cursor()

    def AgregarDetalleMensualTrabajador(self):
        dato = (self.IDEmpleado, self.IDMes, self.detailAnio, self.detailHorasExtra, self.detailMinutosTardanzas, self.detailMinutosJustificados, self.detailDiasFalta, self.detailDiasJustificados, self.detailSueldoNeto)
        consulta = "INSERT INTO tblDetalleMensualTrabajador (IDEmpleado, IDMes, detailAnio, detailHorasExtra, detailMinutosTardanzas, detailMinutosJustificados, detailDiasFalta, detailDiasJustificados, detailSueldoNeto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Detalle mensual del trabajador guardado correctamente')
        except Exception as e:
            pass
        finally:
            self.CerrarConexion()

    def ActualizarDetalleMensualTrabajador(self):
        dato = (self.detailAnio, self.detailHorasExtra, self.detailMinutosTardanzas, self.detailMinutosJustificados, self.detailDiasFalta, self.detailDiasJustificados, self.detailSueldoNeto, self.IDEmpleado, self.IDMes)
        consulta = "UPDATE tblDetalleMensualTrabajador SET detailAnio=?, detailHorasExtra=?, detailMinutosTardanzas=?, detailMinutosJustificados=?, detailDiasFalta=?, detailDiasJustificados=?, detailSueldoNeto=? WHERE IDEmpleado=? AND IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Detalle mensual del trabajador actualizado')
        except Exception as e:
            print(f'Error al actualizar el detalle mensual del trabajador: {e}')
        finally:
            self.CerrarConexion()

    def EliminarDetalleMensualTrabajador(self):
        dato = (self.IDEmpleado, self.IDMes)
        consulta = "DELETE FROM tblDetalleMensualTrabajador WHERE IDEmpleado=? AND IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Detalle mensual del trabajador eliminado')
        except Exception as e:
            print(f'Error al eliminar el detalle mensual del trabajador: {e}')
        finally:
            self.CerrarConexion()

    def LeerDetalleMensualTrabajador(self):
        lista = []
        dato = (self.IDEmpleado, self.IDMes)
        consulta = "SELECT * FROM tblDetalleMensualTrabajador WHERE IDEmpleado=? AND IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            resultado = self.cursor.fetchall()
            if resultado:
                detalleMensualTrabajador = self.cursor.fetchall()
                lista = detalleMensualTrabajador
                lista.reverse()
                return lista
            else:
                mensaje = "Detalle mensual del trabajador no encontrado."
                return mensaje
        except Exception as e:
            print(f'Error al leer el detalle mensual del trabajador: {e}')
        finally:
            self.CerrarConexion()

    def CerrarConexion(self):
        try:
            self.cursor.close()
            self.conexion.close()
        except Exception as e:
            print(f'Error al cerrar la conexión: {e}')
