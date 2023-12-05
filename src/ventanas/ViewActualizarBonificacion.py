
from src.Clases.ClaseBonificacion import SQLBonificacion
import tkinter as tk
from tkinter import ttk , messagebox


def on_combobox_change(*args):
    selected_value = txt.get()
    global id
    if(selected_value=='Movilidad'):
        id='BON001'
    else:
        id = 'BON002'
    consul = SQLBonificacion(id)
    boniActu=consul.LeerBonificacion()[2]
    labeLBoniActual.config(text=f'La bonificacion actual es de: {boniActu}' )


def abrir_ventana3():
    ventana3 = tk.Toplevel()
    ventana3.title("Actualizar Bonificacion")
    ventana3.geometry('430x550')

    # Crear un marco dentro de la ventana3
    frame = tk.Frame(ventana3)
    frame.pack()
    ventana3.configure(bg='#E1735B')
    frame.configure(bg='#E1735B')
    # Crea el label3 dentro del marco
    label3 = tk.Label(frame, text="Tipo de Bonificacion: ")
    label3.config(bg='#E1735B')
    label3.grid(row=0, column=0, pady=30, columnspan=2)

    global txt
    txt = tk.StringVar()
    combo = ttk.Combobox(frame, values=['Movilidad', 'Suplementaria'], textvariable=txt)
    combo['state'] = 'readonly'
    combo.set('Elegir opción')
    combo.grid(row=1, column=0, columnspan=2)

    global labeLBoniActual
    labeLBoniActual = tk.Label(frame, text='')
    labeLBoniActual.config(bg='#E1735B')
    labeLBoniActual.grid(row=2, column=0, pady=40, columnspan=2)

    labeLBoniNueva = tk.Label(frame, text='Nueva Bonificacion: ')
    labeLBoniNueva.grid(row=3, column=0, pady=40)
    labeLBoniNueva.config(bg='#E1735B')

    entryBoni = tk.Entry(frame, text='Nueva Bonificacion')
    entryBoni.grid(row=3, column=1)
    entryBoni.config(bg='#E19989')

    buttonBoni = tk.Button(frame, text='Guardar Cambios',command=lambda : GuardarBoni(entryBoni.get()))
    buttonBoni.grid(row=4, column=0, columnspan=2, pady=50)

    txt.trace_add("write", on_combobox_change)

def GuardarBoni(nuevaBoni):
    boni=SQLBonificacion(id_bonificacion=id,bon_valor=nuevaBoni)
    boni.ActualizarBonificacion()
    labeLBoniActual.config(text=f'La bonificacion actual es de: {nuevaBoni}' )


