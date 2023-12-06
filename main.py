import tkinter as tk
from src.vista import ViewAgregarEmpleado, ViewGestionarEmpleado, ViewActualizarBonificacion

def abrir_ventana(ventana):
    ventana(root)
    root.withdraw()


root = tk.Tk()
root.title("Menú Principal")

root.configure(bg='#27282c')
root.geometry('430x630')
frame = tk.Frame(root)
frame.pack()
frame.configure(bg='#27282c')
img_crear = tk.PhotoImage(file="Recursos/add.png")
img_gestionar = tk.PhotoImage(file="Recursos/gestionarE.png")
img_gestionarB = tk.PhotoImage(file="Recursos/bonificacion.png")
img_imagen = tk.PhotoImage(file="Recursos/logoconti.png")
img_imagenLOBO = tk.PhotoImage(file="Recursos/josueimagen.png")
img_imagentitulo = tk.PhotoImage(file="Recursos/titulo.png")

btn_AgregarEmpleado = tk.Button(frame, image=img_crear, command=lambda: abrir_ventana(
ViewAgregarEmpleado.abrir_ventana1))
btn_AgregarEmpleado.image = img_crear
btn_AgregarEmpleado.config( fg='white', bg='grey', activebackground='green')
btn_AgregarEmpleado.grid(row=1, column=3, padx=10, pady=10)

btn_GestionarEmpleado = tk.Button(frame, image=img_gestionar, command=lambda: abrir_ventana(
ViewGestionarEmpleado.abrir_ventana2))
btn_GestionarEmpleado.image = img_gestionar
btn_GestionarEmpleado.config( bg='grey', activebackground='green')
btn_GestionarEmpleado.grid(row=2, column=3, padx=10, pady=10)

btn_ActualizarBonificacion = tk.Button(frame, image=img_gestionarB, command=lambda: abrir_ventana(
ViewActualizarBonificacion.abrir_ventana3))
btn_ActualizarBonificacion.image = img_gestionarB
btn_ActualizarBonificacion.config( fg='white', bg='grey', activebackground='green')
btn_ActualizarBonificacion.grid(row=3, column=3, padx=10, pady=10)

btn_Salir= tk.Button(frame, text='Salir',command=root.destroy)
btn_Salir.config(font=('Times New Roman', 10, 'bold'), fg='#D01818', bg='#Ce8d8d', activebackground='green')
btn_Salir.grid(row=4, column=3, sticky="ew")


btn_josue = tk.Label(frame, image=img_imagen)
btn_josue.config(fg='white', bg='#27282c', activebackground='green')
btn_josue.grid(row=0, column=2, padx=10, pady=10,   columnspan=3)

lobo = tk.Label(frame, image=img_imagenLOBO)
lobo.config(fg='white', bg='#27282c', activebackground='green')
lobo.grid(row=3, column=5,columnspan=4)

titulo = tk.Label(frame, image=img_imagentitulo)
titulo.config(fg='white', bg='#27282c', activebackground='green')
titulo.grid(row=2, column=5,columnspan=4)


root.mainloop()
