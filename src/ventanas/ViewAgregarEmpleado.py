import tkinter as tk
from tkinter import ttk
from src.Data.conexion_db import Conexion
from src.Clases.ClaseEmpleado import SQLEmpleado


def abrir_ventana1(root):
    ventana1 = tk.Toplevel()
    ventana1.title("Agregar Empleado")
    frameAgregar = tk.Frame(ventana1)
    frameAgregar.pack()
    label_nombre = tk.Label(frameAgregar, text='Nombre Completo: ')
    label_nombre.config(font=('Times New Roman', 14, 'bold'))
    label_nombre.grid(row=0, column=0, padx=10, pady=10)

    label_Sueldo = tk.Label(frameAgregar, text='Sueldo: ')
    label_Sueldo.config(font=('Times New Roman', 14, 'bold'))
    label_Sueldo.grid(row=1, column=0, padx=10, pady=10)

    label_cargo = tk.Label(frameAgregar, text='Cargo: ')
    label_cargo.config(font=('Times New Roman', 14, 'bold'))
    label_cargo.grid(row=2, column=0, padx=10, pady=10)

    frameAgregar.nombre = tk.StringVar()
    frameAgregar.entry_nombre = tk.Entry(frameAgregar, textvariable=frameAgregar.nombre)
    frameAgregar.entry_nombre.config(width=50, font=('Times New Roman', 14))
    frameAgregar.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    frameAgregar.sueldo = tk.StringVar()
    frameAgregar.entry_Sueldo = tk.Entry(frameAgregar, textvariable=frameAgregar.sueldo)
    frameAgregar.entry_Sueldo.config(width=50, font=('Times New Roman', 14))
    frameAgregar.entry_Sueldo.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    frameAgregar.cargo = tk.StringVar()
    frameAgregar.entry_Cargo = tk.Entry(frameAgregar, textvariable=frameAgregar.cargo)
    frameAgregar.entry_Cargo.config(width=50, font=('Times New Roman', 14))
    frameAgregar.entry_Cargo.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    frameAgregar.boton_nuevo = tk.Button(frameAgregar, text='Nuevo', command=lambda: habilitar_campos(frameAgregar))
    frameAgregar.boton_nuevo.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                                    activebackground='green')
    frameAgregar.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

    frameAgregar.boton_guardar = tk.Button(frameAgregar, text='Guardar', command=lambda: guardar_datos(frameAgregar))
    frameAgregar.boton_guardar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                                      activebackground='green')
    frameAgregar.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

    frameAgregar.boton_cancelar = tk.Button(frameAgregar, text='Cancelar',
                                            command=lambda: deshabilitar_campos(frameAgregar))
    frameAgregar.boton_cancelar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Red', bg='Orange',
                                       activebackground='green')
    frameAgregar.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    frameAgregar.boton_Eliminar = tk.Button(frameAgregar, text='Eliminar', command=lambda: Eliminar(frameAgregar))
    frameAgregar.boton_Eliminar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Yellow', bg='Red',
                                       activebackground='green')
    frameAgregar.boton_Eliminar.grid(row=6, column=1, padx=10, pady=10)

    frameAgregar.boton_Editar = tk.Button(frameAgregar, text='Editar', command=lambda: Editar(frameAgregar))
    frameAgregar.boton_Editar.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Yellow', bg='Green',
                                     activebackground='green')
    frameAgregar.boton_Editar.grid(row=6, column=0, padx=10, pady=10)

    frameAgregar.boton_volver = tk.Button(frameAgregar, text='volver',command=lambda: volver(ventana1,root))
    frameAgregar.boton_volver.config(width=20, font=('Times New Roman', 14, 'bold'), fg='Yellow', bg='Green',
                                     activebackground='gray')
    frameAgregar.boton_volver.grid(row=7, column=2, padx=10, pady=10)



    tabla_empleado(frameAgregar)
    deshabilitar_campos(frameAgregar)


def volver(ventana,root):
    ventana.withdraw()
    root.deiconify()
def deshabilitar_campos(frameAgregar):
    frameAgregar.entry_Cargo.config(state='disable')
    frameAgregar.entry_Sueldo.config(state='disable')
    frameAgregar.entry_nombre.config(state='disable')
    frameAgregar.boton_guardar.config(state='disable')
    frameAgregar.boton_cancelar.config(state='disable')
    frameAgregar.nombre.set('')
    frameAgregar.sueldo.set('')
    frameAgregar.cargo.set('')


def habilitar_campos(frameAgregar):
    frameAgregar.valor = 0
    frameAgregar.entry_Cargo.config(state='normal')
    frameAgregar.entry_Sueldo.config(state='normal')
    frameAgregar.entry_nombre.config(state='normal')
    frameAgregar.boton_guardar.config(state='normal')
    frameAgregar.boton_cancelar.config(state='normal')


def guardar_datos(frameAgregar):
    nombre = frameAgregar.entry_nombre.get()
    sueldo = frameAgregar.sueldo.get()
    cargo = frameAgregar.cargo.get()

    if (frameAgregar.valor == 0):
        conexion = Conexion()
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

        empleado = SQLEmpleado(nuevo_id, nombre, sueldo, cargo)
        empleado.AgregarEmpleado()

    else:
        empleado2 = SQLEmpleado(frameAgregar.valor, nombre, sueldo, cargo)
        empleado2.ActualizarEmpleado()

    tabla_empleado(frameAgregar)
    deshabilitar_campos(frameAgregar)
    frameAgregar.valor = 0


def tabla_empleado(frameAgregar):
    frameAgregar.tabla = ttk.Treeview(frameAgregar, column=('Nombre', 'Sueldo', 'Cargo'))
    frameAgregar.tabla.grid(row=5, column=0, columnspan=4)
    frameAgregar.tabla.heading('#0', text='ID')
    frameAgregar.tabla.heading('#1', text='Nombre')
    frameAgregar.tabla.heading('#2', text='Sueldo')
    frameAgregar.tabla.heading('#3', text='Cargo')

    empleado = SQLEmpleado()
    frameAgregar.lista = empleado.DatosCompletos()
    for i in frameAgregar.lista:
        frameAgregar.tabla.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))

    for col in ('#0', '#1', '#2', '#3'):
        frameAgregar.tabla.column(col, anchor='center')


def Eliminar(frameAgregar):
    selected_item = frameAgregar.tabla.selection()
    if selected_item:
        selected_row = frameAgregar.tabla.item(selected_item)
        id = selected_row['text']  # ID en la columna 0
    empleado = SQLEmpleado(id)
    empleado.EliminarEmpleado()
    tabla_empleado(frameAgregar)


def Editar(frameAgregar):
    selected_item = frameAgregar.tabla.selection()
    if selected_item:
        selected_row = frameAgregar.tabla.item(selected_item)
        id = selected_row['text']
        nombre = selected_row['values'][0]  # Nombre en la columna 1
        sueldo = selected_row['values'][1]  # Sueldo en la columna 2
        cargo = selected_row['values'][2]  # Cargo en la columna 3
    habilitar_campos(frameAgregar)
    frameAgregar.nombre.set(nombre)
    frameAgregar.sueldo.set(sueldo)
    frameAgregar.cargo.set(cargo)
    frameAgregar.valor = id








