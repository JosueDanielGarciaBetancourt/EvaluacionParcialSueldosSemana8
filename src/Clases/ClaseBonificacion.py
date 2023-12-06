from src.modelo.conexion_db import Conexion
from tkinter import messagebox

class SQLBonificacion:
    def __init__(self, id_bonificacion=None, bon_tipo=None, bon_valor=None):
        self.id_bonificacion = id_bonificacion
        self.bon_tipo = bon_tipo
        self.bon_valor = bon_valor

        self.conexion = Conexion()
        self.cursor = self.conexion.cursor()

    def AgregarBonificacion(self):
        dato = (self.id_bonificacion, self.bon_tipo, self.bon_valor)
        consulta = "INSERT INTO tblBonificacion (IDBonificacion, bonTipo, bonValor) VALUES (?, ?, ?)"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            messagebox.showinfo('Mensaje', 'Bonificación agregada correctamente')
        except Exception as e:
            messagebox.showinfo('Mensaje de error', f'Error al agregar bonificación: {e}')
        finally:
            self.CerrarConexion()

    def ActualizarBonificacion(self):
        dato = (self.bon_valor,self.id_bonificacion)
        consulta = "UPDATE tblBonificacion SET bonValor=? WHERE IDBonificacion=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            messagebox.showinfo('Bonificación actualizada')
        except Exception as e:
            messagebox.showerror(f'Error al actualizar bonificación: {e}')
        finally:
            self.CerrarConexion()

    def EliminarBonificacion(self):
        dato = (self.id_bonificacion,)
        consulta = "DELETE FROM tblBonificacion WHERE IDBonificacion=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Bonificación eliminada')
        except Exception as e:
            print(f'Error al eliminar bonificación: {e}')
        finally:
            self.CerrarConexion()

    def LeerBonificacion(self):
        lista=[]
        dato = (self.id_bonificacion)
        consulta = "SELECT * FROM tblBonificacion WHERE IDBonificacion=?"
        try:
            self.cursor.execute(consulta, dato)
            resultado = self.cursor.fetchone()
            if resultado:
                lista = resultado
            else:
                mensaje = "Bonificación no encontrada."
                return mensaje
        except Exception as e:
            print(f'Error al leer bonificación: {e}')
        finally:
            self.CerrarConexion()

        return lista

    def DatosCompletos(self):
        self.cursor.execute("SELECT * FROM tblBonificacion;")
        lista = self.cursor.fetchall()
        return lista

    def CerrarConexion(self):
        try:
            self.cursor.close()
            self.conexion.close()
        except Exception as e:
            print(f'Error al cerrar la conexión: {e}')