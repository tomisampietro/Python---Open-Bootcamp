import tkinter as tk

# Crea la ventana principal
window = tk.Tk()
window.title("Interfaz con lista y label")

# Crea una lista de elementos
elements = ["Elemento 1", "Elemento 2", "Elemento 3"]

# Crea una lista desplegable y un label
listbox = tk.Listbox(window)
label = tk.Label(window, text="")

# Añade los elementos a la lista desplegable
for element in elements:
    listbox.insert(tk.END, element)

# Crea una función para mostrar el elemento seleccionado en el label
def show_selection():
    index = listbox.curselection()[0]
    label.config(text=elements[index])

# Añade un botón para mostrar la selección
tk.Button(window, text="Mostrar selección", command=show_selection).pack()

# Empaqueta la lista desplegable y el label
listbox.pack()
label.pack()

# Ejecuta el bucle de eventos
window.mainloop()
