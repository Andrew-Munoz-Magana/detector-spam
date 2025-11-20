import tkinter as tk


from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Botón presionado!")


ventana = tk.Tk()   #Crear ventana principal
ventana.title("Ventana simple") #Le da nombre a la ventana


label = tk.Label(ventana, text="Hola, mundo!")  # Crea un widget de texto
label.pack()    # Lo coloca en la ventana

boton = tk.Button(ventana, text="Haz click aquí")
boton.pack()


label = tk.Label(ventana, text="Presiona el botón para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz click aquí", command=mostrar_mensaje)
boton.pack(pady=10)


ventana.mainloop()  #Mostrar ventana