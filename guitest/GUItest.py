import tkinter as tk
import tkinter.messagebox
def agregar_personal():
    # Crear una nueva ventana
    ventana = tk.Toplevel(root)
    # Darle un título
    ventana.title("Agregar personal")
    # Crear los widgets para pedir información
    etiqueta_nombre = tk.Label(ventana, text="Nombre:")
    entrada_nombre = tk.Entry(ventana)
    etiqueta_dni = tk.Label(ventana, text="DNI:")
    entrada_dni = tk.Entry(ventana)
    etiqueta_sueldo = tk.Label(ventana, text="Sueldo:")
    entrada_sueldo = tk.Entry(ventana)
    etiqueta_puesto = tk.Label(ventana, text="Puesto:")
    entrada_puesto = tk.Entry(ventana)
    boton_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_a_bd(entrada_nombre.get(), entrada_dni.get(), entrada_sueldo.get(), entrada_puesto.get()))
    # Colocar los widgets en la ventana usando el administrador de geometría grid
    etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)
    entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
    etiqueta_dni.grid(row=1, column=0, padx=5, pady=5)
    entrada_dni.grid(row=1, column=1, padx=5, pady=5)
    etiqueta_sueldo.grid(row=2, column=0, padx=5, pady=5)
    entrada_sueldo.grid(row=2, column=1, padx=5, pady=5)
    etiqueta_puesto.grid(row=3, column=0, padx=5, pady=5)
    entrada_puesto.grid(row=3, column=1, padx=5, pady=5)
    boton_agregar.grid(row=4, columnspan=2, padx=5, pady=5)

def buscar_personal():
    # Crear una nueva ventana
    ventana = tk.Toplevel(root)
    # Darle un título
    ventana.title("Buscar personal")
    # Crear los widgets para pedir y mostrar información
    etiqueta_buscar = tk.Label(ventana, text="Buscar por:")
    entrada_buscar = tk.Entry(ventana)
    boton_buscar = tk.Button(ventana, text="Buscar", command=lambda: buscar_en_bd(entrada_buscar.get()))
    lista_resultados = tk.Listbox(ventana)
    # Colocar los widgets en la ventana usando el administrador de geometría grid
    etiqueta_buscar.grid(row=0, column=0, padx=5, pady=5)
    entrada_buscar.grid(row=0, column=1, padx=5, pady=5)
    boton_buscar.grid(row=0, columnspan=2, padx=5, pady=5)
    lista_resultados.grid(row=1, columnspan=3)

def actualizar_bonificacion():
    # Crear una nueva ventana
    ventana = tk.Toplevel(root)
    # Darle un título
    ventana.title("Actualizar bonificación")
    # Crear los widgets para pedir y cambiar información
    etiqueta_tipo = tk.Label(ventana, text="Tipo de bonificación:")
    opciones_tipo = ["Bonificación por antigüedad", "Bonificación por desempeño"]
    variable_tipo = tk.StringVar()
    variable_tipo.set(opciones_tipo[0])
    menu_tipo = tk.OptionMenu(ventana, variable_tipo, *opciones_tipo)
    etiqueta_valor = tk.Label(ventana, text="Nuevo valor:")
    entrada_valor = tk.Entry(ventana)
    boton_actualizar = tk.Button(ventana,text="Actualizar", command=lambda: actualizar_en_bd(variable_tipo.get(), entrada_valor.get()))
     # Colocar los widgets en la ventana usando el administrador de geometría grid
    etiqueta_tipo.grid(row=0, column=0, padx=5, pady=5)
    menu_tipo.grid(row=0, column=1, padx=5, pady=5)
    etiqueta_valor.grid(row=1, column=0, padx=5, pady=5)
    entrada_valor.grid(row=1, column=1, padx=5, pady=5)
    boton_actualizar.grid(row=2, columnspan=2, padx=5, pady=5)

def salir():
    root.destroy()

def agregar_a_bd(nombre, dni, sueldo, puesto):
    # Aquí debes escribir el código para agregar los datos del personal a la base de datos
    print("Agregar a la base de datos")
    # Mostrar una ventana de confirmación
    tkinter.messagebox.showinfo("Confirmación", "Se ha agregado el personal correctamente")

def buscar_en_bd(criterio):
    # Aquí debes escribir el código para buscar los datos del personal en la base de datos según el criterio
    print("Buscar en la base de datos")
    # Mostrar los resultados en el widget Listbox
    lista_resultados.insert(0, "Resultado 1")
    lista_resultados.insert(1, "Resultado 2")

def actualizar_en_bd(tipo, valor):
    # Aquí debes escribir el código para actualizar el valor de la bonificación en la base de datos según el tipo
    print("Actualizar en la base de datos")
    # Mostrar una ventana de confirmación
    tkinter.messagebox.showinfo("Confirmación", "Se ha actualizado la bonificación correctamente")

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

personal_menu = tk.Menu(menu)
menu.add_cascade(label="Personal", menu=personal_menu)
personal_menu.add_command(label="Agregar personal", command=agregar_personal)
personal_menu.add_command(label="Buscar personal", command=buscar_personal)

bonificacion_menu = tk.Menu(menu)
menu.add_cascade(label="Bonificación", menu=bonificacion_menu)
bonificacion_menu.add_command(label="Actualizar bonificación", command=actualizar_bonificacion)

menu.add_command(label="Salir", command=salir)

root.mainloop()