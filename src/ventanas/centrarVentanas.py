class centrar:
    def centrar_ventana(ventana):
        ventana.update_idletasks()
        ancho_ventana = ventana.winfo_width()
        alto_ventana = ventana.winfo_height()
        x_ventana = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y_ventana = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry('+{}+{}'.format(x_ventana, y_ventana))