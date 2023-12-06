from src.modelo.conexion_db import Conexion
from tkinter import messagebox
class SQLEmpleado:
    def __init__(self, id=None, nombre=None, sueldo=None, cargo=None):
        self.id = id
        self.nombre = nombre
        self.sueldo = sueldo
        self.cargo = cargo
        self.conexion = Conexion()
        self.cursor = self.conexion.cursor()

    def AgregarEmpleado(self):
        dato = [(self.id, self.nombre, self.sueldo, self.cargo)]
        self.cursor = self.conexion.cursor()
        try:
            self.cursor.executemany(f"INSERT INTO Empleado VALUES (?, ?, ?, ?)", dato)
            self.conexion.commit()  # Realiza la confirmación para guardar los cambios
            messagebox.showinfo('Mensaje','Se guardo correctamente')
        except Exception as e:
            messagebox.showinfo('Mensaje de error', f'Error al guardar: {e}')
        finally:
            self.CerrarConexion()

    def ActualizarEmpleado(self):
        dato = (self.sueldo, self.nombre, self.cargo, self.id)
        consulta = "UPDATE Empleado SET Sueldo=?, NombreCompleto=?, Cargo=? WHERE id=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Empleado actualizado')
        except Exception as e:
            print(f'Error al actualizar empleado: {e}')
        finally:
            self.CerrarConexion()

    def EliminarEmpleado(self):
        dato = (self.id,)
        consulta = "DELETE FROM Empleado WHERE id=?"
        try:
            self.cursor.execute(consulta, dato)
            self.conexion.commit()
            print('Empleado eliminado')
        except Exception as e:
            print(f'Error al eliminar empleado: {e}')
        finally:
            self.CerrarConexion()

    def LeerEmpleado(self):
            lista = []
            consulta = ""
            if self.id:
                dato = (self.id,)
                consulta = "SELECT * FROM Empleado WHERE ID = ?"
            else:
                dato = (f'%{self.nombre}%',)
                consulta = "SELECT * FROM Empleado WHERE NombreCompleto LIKE ?"

            try:
                self.cursor.execute(consulta, dato)
                resultado = self.cursor.fetchall()
                if resultado:
                    lista = resultado
                    lista.reverse()
                else:
                    messagebox.showerror('Mensaje', "Empleado no encontrado.")
            except Exception as e:
                print(f'Error al leer empleado: {e}')
            finally:
                self.CerrarConexion()

            return lista

    def DatosCompletos(self):
        self.cursor.execute("Select * from Empleado;")
        lista = []
        Empleado = self.cursor.fetchall()
        lista = Empleado
        lista.reverse()
        return lista
    def CerrarConexion(self):
        try:
            self.cursor.close()
            self.conexion.close()
        except Exception as e:
            print(f'Error al cerrar la conexión: {e}')



