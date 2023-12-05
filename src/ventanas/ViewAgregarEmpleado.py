import tkinter as tk
from tkinter import ttk
from src.Data.conexion_db import Conexion
from src.Clases.ClaseEmpleado import SQLEmpleado


def abrir_ventana1():
    global valor
    ventana1 = tk.Toplevel()
    ventana1.title("Agregar Empleado")
    ventana1.geometry("800x600")

    label_nombre = tk.Label(ventana1, text='Nombre Completo: ')
    label_nombre.config(font=('Times New Roman', 14, 'bold'))
    label_nombre.grid(row=0, column=0, padx=10, pady=10)

    label_Sueldo = tk.Label(ventana1, text='Sueldo: ')
    label_Sueldo.config(font=('Times New Roman', 14, 'bold'))
    label_Sueldo.grid(row=1, column=0, padx=10, pady=10)

    label_cargo = tk.Label(ventana1, text='Cargo: ')
    label_cargo.config(font=('Times New Roman', 14, 'bold'))
    label_cargo.grid(row=2, column=0, padx=10, pady=10)

    ventana1.nombre = tk.StringVar()
    ventana1.entry_nombre = tk.Entry(ventana1, textvariable=ventana1.nombre)
    ventana1.entry_nombre.config(width=50, font=('Times New Roman', 14))
    ventana1.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    ventana1.sueldo = tk.StringVar()
    ventana1.entry_Sueldo = tk.Entry(ventana1, textvariable=ventana1.sueldo)
    ventana1.entry_Sueldo.config(width=50, font=('Times New Roman', 14))
    ventana1.entry_Sueldo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    ventana1.cargo = tk.StringVar()
    ventana1.entry_Cargo = tk.Entry(ventana1, textvariable=ventana1.cargo)
    ventana1.entry_Cargo.config(width=50, font=('Times New Roman', 14))
    ventana1.entry_Cargo.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    ventana1.boton_nuevo = tk.Button(ventana1, text='Nuevo', command=lambda: habilitar_campos(ventana1))
    ventana1.boton_nuevo.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                            activebackground='green')
    ventana1.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

    ventana1.boton_guardar = tk.Button(ventana1, text='Guardar', command=lambda: guardar_datos(ventana1))
    ventana1.boton_guardar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                                activebackground='green')
    ventana1.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

    ventana1.boton_cancelar = tk.Button(ventana1, text='Cancelar', command=lambda: deshabilitar_campos(ventana1))
    ventana1.boton_cancelar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                                activebackground='green')
    ventana1.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    ventana1.boton_Eliminar = tk.Button(ventana1, text='Eliminar',command=lambda :Eliminar(ventana1))
    ventana1.boton_Eliminar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Yellow', bg='Red',
                                activebackground='green')
    ventana1.boton_Eliminar.grid(row=6, column=1, padx=10, pady=10)

    ventana1.boton_Editar = tk.Button(ventana1, text='Editar',command=lambda :Editar(ventana1))
    ventana1.boton_Editar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Yellow', bg='Green',
                                activebackground='green')
    ventana1.boton_Editar.grid(row=6, column=0, padx=10, pady=10)

    tabla_empleado(ventana1)
    deshabilitar_campos(ventana1)



def deshabilitar_campos(ventana1):
    ventana1.entry_Cargo.config(state='disable')
    ventana1.entry_Sueldo.config(state='disable')
    ventana1.entry_nombre.config(state='disable')
    ventana1.boton_guardar.config(state='disable')
    ventana1.boton_cancelar.config(state='disable')
    ventana1.nombre.set('')
    ventana1.sueldo.set('')
    ventana1.cargo.set('')

def habilitar_campos(ventana1):
    ventana1.valor=0
    ventana1.entry_Cargo.config(state='normal')
    ventana1.entry_Sueldo.config(state='normal')
    ventana1.entry_nombre.config(state='normal')
    ventana1.boton_guardar.config(state='normal')
    ventana1.boton_cancelar.config(state='normal')

def guardar_datos(ventana1):
    nombre = ventana1.entry_nombre.get()
    sueldo = ventana1.sueldo.get()
    cargo = ventana1.cargo.get()

    if(ventana1.valor==0):
        conexion=Conexion()
        # Obtén el último ID
        cursor = conexion.cursor()
        cursor.execute('SELECT MAX(ID) as UltimoID FROM Empleado;')
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()


        if resultado and resultado.UltimoID is not None:
            ultimo_id = resultado.UltimoID
            nuevo_id = ultimo_id + 1
        else:
            # Si no se encontraron registros, establece el nuevo ID en 1
            nuevo_id = 1

        empleado=SQLEmpleado(nuevo_id,nombre,sueldo,cargo)
        empleado.AgregarEmpleado()

    else:
        empleado2=SQLEmpleado(ventana1.valor,nombre,sueldo,cargo)
        empleado2.ActualizarEmpleado()

    tabla_empleado(ventana1)
    deshabilitar_campos(ventana1)
    ventana1.valor=0
def tabla_empleado(ventana1):
    ventana1.tabla = ttk.Treeview(ventana1, column=('Nombre', 'Sueldo', 'Cargo'))
    ventana1.tabla.grid(row=5, column=0, columnspan=4)
    ventana1.tabla.heading('#0', text='ID')
    ventana1.tabla.heading('#1', text='Nombre')
    ventana1.tabla.heading('#2', text='Sueldo')
    ventana1.tabla.heading('#3', text='Cargo')

    empleado=SQLEmpleado()
    ventana1.lista=empleado.DatosCompletos()
    for i in ventana1.lista:
        ventana1.tabla.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))

    for col in ('#0', '#1', '#2', '#3'):
        ventana1.tabla.column(col, anchor='center')

def Eliminar(ventana1):
    selected_item = ventana1.tabla.selection()
    if selected_item:
        selected_row = ventana1.tabla.item(selected_item)
        id = selected_row['text']  # ID en la columna 0
    empleado=SQLEmpleado(id)
    empleado.EliminarEmpleado()
    tabla_empleado(ventana1)


def Editar(ventana1):
    selected_item = ventana1.tabla.selection()
    if selected_item:
        selected_row = ventana1.tabla.item(selected_item)
        id=selected_row['text']
        nombre = selected_row['values'][0]  # Nombre en la columna 1
        sueldo = selected_row['values'][1]  # Sueldo en la columna 2
        cargo = selected_row['values'][2]  # Cargo en la columna 3
    habilitar_campos(ventana1)
    ventana1.nombre.set(nombre)
    ventana1.sueldo.set(sueldo)
    ventana1.cargo.set(cargo)
    ventana1.valor=id







