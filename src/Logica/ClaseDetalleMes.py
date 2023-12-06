from src.modelo.conexion_db import Conexion
from tkinter import messagebox

class SQLMes:
    def __init__(self, id_mes=None, mes_nombre=None):
        self.id_mes = id_mes
        self.mes_nombre = mes_nombre

        self.conexion = Conexion()
        self.cursor = self.conexion.cursor()

    def AgregarMes(self):
        dato = (self.id_mes, self.mes_nombre)
        consulta = "INSERT INTO tblMes (IDMes, mesNombre) VALUES (?, ?)"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
        except Exception as e:
                pass
        finally:
            self.CerrarConexion()
            print('waaa')

    def ActualizarMes(self):
        dato = (self.mes_nombre, self.id_mes)
        consulta = "UPDATE tblMes SET mesNombre=? WHERE IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Mes actualizado')
        except Exception as e:
            print(f'Error al actualizar mes: {e}')
        finally:
            self.CerrarConexion()

    def EliminarMes(self):
        dato = (self.id_mes,)
        consulta = "DELETE FROM tblMes WHERE IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Mes eliminado')
        except Exception as e:
            print(f'Error al eliminar mes: {e}')
        finally:
            self.CerrarConexion()

    def LeerMes(self):
        lista = 0
        dato = (self.id_mes,)
        consulta = "SELECT * FROM tblMes WHERE IDMes=?"
        try:
            self.cursor.execute(consulta, dato)
            resultado = self.cursor.fetchall()

            if resultado:
                lista = 1
            else:
                lista= 0

        except Exception as e:
            print(f'Error al leer: {e}')

        return lista

    def DatosCompletos(self):
        self.cursor.execute("SELECT * FROM tblMes;")
        lista = self.cursor.fetchall()
        return lista

    def CerrarConexion(self):
        try:
            self.cursor.close()
            self.conexion.close()
        except Exception as e:
            print(f'Error al cerrar la conexión: {e}')