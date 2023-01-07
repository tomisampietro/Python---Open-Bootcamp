import tkinter as tk

# Crea la ventana principal
window = tk.Tk()
window.title("Lista de RadioButton")

# Crea una lista de opciones
options = ["Opción 1", "Opción 2", "Opción 3"]

# Crea una variable para almacenar la opción seleccionada
selected_option = tk.StringVar()

# Crea una función para reiniciar la selección
def reset_selection():
    selected_option.set("")

# Crea una función para mostrar la opción seleccionada
def show_selection():
    print(selected_option.get())

# Crea una fila para cada opción
for index, option in enumerate(options):
    tk.Radiobutton(window, text=option, variable=selected_option, value=option).pack()

# Crea un botón de reinicio y un botón para mostrar la opción seleccionada
tk.Button(window, text="Reiniciar", command=reset_selection).pack()
tk.Button(window, text="Mostrar selección", command=show_selection).pack()

# Ejecuta el bucle de eventos
window.mainloop()
