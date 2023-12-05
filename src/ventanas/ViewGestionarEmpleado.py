import tkinter as tk
from tkinter import ttk
from src.Data.conexion_db import Conexion
from src.Clases.ClaseDetalleMensualTrabajador import SQLDetalleMensualTrabajador
from src.Clases.ClaseDetalleMes import SQLMes
from src.Clases.ClaseEmpleado import SQLEmpleado
from src.Logica.CalculoSueldo import calcularSueldo
from src.Clases.ClaseBonificacion import SQLBonificacion
from src.Clases.ClaseBoletaPago import SQLBoletaPago
from datetime import datetime
from src.Clases.ClasePDF import GeneradorBoletaPago

def abrir_ventana2(root):
    global ventanaGE1
    ventanaGE1 = tk.Toplevel()
    ventanaGE1.title('Buscar Empleado')
    ventanaGE1.geometry("600x400")

    ventanaGE = tk.Frame(ventanaGE1)
    ventanaGE.label = tk.Label(ventanaGE1, text="Nombre del Empleado:")
    ventanaGE.label.grid(row=0, column=0, padx=10, pady=10)
    ventanaGE.entry = tk.Entry(ventanaGE1)
    ventanaGE.entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    ventanaGE.botonBuscar = tk.Button(ventanaGE1, text='Buscar Empleado', command=lambda: BuscarEmpleado(ventanaGE))
    ventanaGE.botonBuscar.config(bg='Green', fg='White')
    ventanaGE.botonBuscar.grid(row=1, column=1, padx=10, pady=10)

    ventanaGE.tablaB = ttk.Treeview(ventanaGE1, column=('Nombre', 'Cargo'))
    ventanaGE.tablaB.grid(row=2, column=0, columnspan=3)
    ventanaGE.tablaB.heading('#0', text='ID')
    ventanaGE.tablaB.heading('#1', text='Nombre')
    ventanaGE.tablaB.heading('#2', text='Cargo')

    ventanaGE.botonSeleccionar = tk.Button(ventanaGE1, text='Mostrar Historial', command=lambda: Seleccion1(ventanaGE))
    ventanaGE.botonSeleccionar.config(bg='grey', fg='White')
    ventanaGE.botonSeleccionar.grid(row=3, column=1, padx=10, pady=10)

    ventanaGE.botonSeleccionar2 = tk.Button(ventanaGE1, text='Crear Nuevo Sueldo',
                                            command=lambda: Seleccion2(ventanaGE))
    ventanaGE.botonSeleccionar2.config(bg='grey', fg='White')
    ventanaGE.botonSeleccionar2.grid(row=3, column=2, padx=10, pady=10)


    ventanaGE.volver = tk.Button(ventanaGE1, text='volver',
                                            command=lambda: volver(ventanaGE1,root))
    ventanaGE.volver.config(bg='grey', fg='White')
    ventanaGE.volver.grid(row=4, column=2, padx=10, pady=10)


    ventanaGE.tablaB.bind('<ButtonRelease-1>', lambda event: habilitar(ventanaGE))

    deshabilitar(ventanaGE)


def volver(ventana,root):
    ventana.withdraw()
    root.deiconify()

def BuscarEmpleado(ventanaGE):
    ventanaGE.tablaB.delete(*ventanaGE.tablaB.get_children())
    nombre = ventanaGE.entry.get()
    empleado = SQLEmpleado(nombre=nombre)
    ventanaGE.lista = empleado.LeerEmpleado()
    for i in ventanaGE.lista:
        ventanaGE.tablaB.insert('', 0, text=i[0], values=(i[1], i[3]))
    deshabilitar(ventanaGE)


def Seleccion1(ventanaGE):
    selected_item = ventanaGE.tablaB.selection()
    global ide
    if selected_item:
        selected_row = ventanaGE.tablaB.item(selected_item)
        ventanaGE.id = selected_row['text']  # ID en la columna 0
        ide=ventanaGE.id
        ventanaGE.nombre = selected_row['values'][0]  # Nombre en la columna 1
    conexion = Conexion()
    cursor = conexion.cursor()
    cursor.execute(f"select * from tblBoletaPago Where IDEmpleado LIKE {ventanaGE.id}")
    lista = cursor.fetchall()
    lista.reverse()

    FrameHistorial = tk.Toplevel()
    FrameHistorial.title('Historial de pagos')
    FrameHistorial.geometry("600x400")
    FrameHistorial.label = tk.Label(FrameHistorial, text=f"Nombre del Empleado: {ventanaGE.nombre}")
    FrameHistorial.label.grid(row=0, column=0, padx=10, pady=10)

    global tablaBOL
    tablaBOL = ttk.Treeview(FrameHistorial, column=('Fecha', 'Monto'))
    tablaBOL.grid(row=2, column=0, columnspan=3)
    tablaBOL.heading('#0', text='ID de Boleta')
    tablaBOL.heading('#1', text='Fecha de pago')
    tablaBOL.heading('#2', text='Monto Total')

    for i in lista:
        tablaBOL.insert('', 0, text=i[0], values=(i[4], i[1]))

    boton = tk.Button(FrameHistorial, text='Ver detalle', command=lambda: VerDetalle())
    boton.grid(row=3, column=0, columnspan=3)
    cursor.close()
    conexion.close()
def VerDetalle():
    selected_item = tablaBOL.selection()
    if selected_item:
        selected_row = tablaBOL.item(selected_item)
        id = selected_row['text']  # ID en la columna 0

    GeneradorBoletaPago(id_boleta=id,id_empleado=ide)



def Seleccion2(ventanaGE):
    global ventanaCrearNuevoSueldo
    ventanaCrearNuevoSueldo = tk.Toplevel()
    ventanaCrearNuevoSueldo.title('Crear Nuevo Sueldo')

    # Crea un Frame dentro de la ventana principal
    frameCrear = tk.Frame(ventanaCrearNuevoSueldo)
    frameCrear.pack(padx=10, pady=10)

    selected_item = ventanaGE.tablaB.selection()

    if selected_item:
        selected_row = ventanaGE.tablaB.item(selected_item)
        ventanaGE.id = selected_row['text']  # ID en la columna 0

    label_horas_extra = tk.Label(frameCrear, text="Horas Extra:")
    label_horas_extra.grid(row=3, column=0, padx=10, pady=10)

    entry_horas_extra = tk.Entry(frameCrear)
    entry_horas_extra.grid(row=3, column=1, padx=10, pady=10)

    label_minutos_falta = tk.Label(frameCrear, text="Minutos de Falta:")
    label_minutos_falta.grid(row=4, column=0, padx=10, pady=10)

    entry_minutos_falta = tk.Entry(frameCrear)
    entry_minutos_falta.grid(row=4, column=1, padx=10, pady=10)

    label_dias_falta = tk.Label(frameCrear, text="Días de Falta:")
    label_dias_falta.grid(row=5, column=0, padx=10, pady=10)

    entry_dias_falta = tk.Entry(frameCrear)
    entry_dias_falta.grid(row=5, column=1, padx=10, pady=10)

    botonGuarda = tk.Button(frameCrear, text='Guardar',
                            command=lambda: GuardarDATOSEMPLEDO(ventanaGE.id, frameCrear))
    botonGuarda.config(bg='grey', fg='White')
    botonGuarda.grid(row=6, column=2, padx=10, pady=10)

def GuardarDATOSEMPLEDO(id, ventana):
    fecha = datetime.now()
    anio = fecha.year
    mes = fecha.month
    mes = f'MES00{mes}{anio}'
    nombremes = fecha.strftime('%B')

    detallemes = SQLMes(mes, nombremes)
    consultames = detallemes.LeerMes()

    horas = int(ventana.children['!entry'].get())
    minutos = int(ventana.children['!entry2'].get())
    dias = int(ventana.children['!entry3'].get())

    if horas == None:
        horas = 0
    if minutos == None:
        minutos = 0
    if dias == None:
        dias = 0

    if consultames == 1:
        detallemesEmpleado = SQLDetalleMensualTrabajador(id, mes, anio, horas, minutos, detailDiasFalta=dias)

    else:
        detallemes.AgregarMes()
        detallemesEmpleado = SQLDetalleMensualTrabajador(id, mes, anio, horas, minutos, detailDiasFalta=dias)

    detallemesEmpleado.AgregarDetalleMensualTrabajador()

    empleado = SQLEmpleado(id=id)
    sueldo = empleado.LeerEmpleado()[0][2]
    bon1 = SQLBonificacion(id_bonificacion='BON001')
    bon2 = SQLBonificacion(id_bonificacion='BON002')
    movilidad = bon1.LeerBonificacion()[2]
    suplementaria = bon2.LeerBonificacion()[2]
    sueldo = float(sueldo)
    sueldope = calcularSueldo(sueldo=sueldo, horasExtra=horas, diasFalta=dias, minutosTardanza=minutos,
                              Movilidad=movilidad, Suplementaria=suplementaria)

    sueldoNeto = sueldope.CalcularSueldoNeto()
    descuentoTotal = sueldope.CalculoDescuentos()
    bonificacionTotal = sueldope.CalculoBonificaciones()

    fecha_actual = datetime.now()
    fecha2 = fecha_actual.strftime("%Y-%m-%d")

    idbol = SQLBoletaPago()
    idbol = idbol.ObtenerUltimoCodigo()
    num = int(idbol[-3:]) + 1
    if num < 10:
        id2 = f'BP00{num}'
    elif num < 100:
        id2 = f'BP0{num}'
    else:
        id2 = f'BP{num}'

    boleta = SQLBoletaPago(id2, sueldoNeto, descuentoTotal, bonificacionTotal, fecha2, id)
    boleta.AgregarBoletaPago()
    ventanaGE1.destroy()

def deshabilitar(ventanaGE):
    ventanaGE.botonSeleccionar.grid_remove()
    ventanaGE.botonSeleccionar2.grid_remove()


def habilitar(ventanaGE):
    ventanaGE.botonSeleccionar.grid()
    ventanaGE.botonSeleccionar2.grid()
