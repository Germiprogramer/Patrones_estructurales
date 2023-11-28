import tkinter as tk
import csv
from tkinter import messagebox
import sys
from interfaces.interfaz_eleccion import interfaz_eleccion

sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio1\datos")

def interfaz_registro():
# Función para registrar al usuario en el CSV
    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        # Verificar si el usuario ya está registrado en el CSV
        with open('ejercicio1/datos/clientes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if username == row[0]:
                    messagebox.showerror("Error", "Usuario ya registrado")
                    return

        # Si no está registrado, agregar el usuario al CSV
        with open('ejercicio1/datos/clientes.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, name_entry.get(), address_entry.get(), phone_entry.get(), email_entry.get(), 0, 100])

        messagebox.showinfo("Registro Exitoso", "Usuario registrado con éxito")
        root.destroy()
        interfaz_eleccion()


    # Función para iniciar sesión
    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Verificar si el usuario y la contraseña coinciden en el CSV
        with open('ejercicio1/datos/clientes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if username == row[0] and password == row[1]:
                    messagebox.showinfo("Inicio de Sesión Exitoso", "Inicio de sesión exitoso")
                    root.destroy()
                    interfaz_eleccion()
                    return
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        
        

    root = tk.Tk()
    root.title("Pizzería")

    # Crear y colocar widgets para el registro del usuario
    tk.Label(root, text="Registro de Usuario").grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(root, text="Usuario").grid(row=1, column=0, padx=10)
    username_entry = tk.Entry(root)
    username_entry.grid(row=2, column=0, padx=10)
    tk.Label(root, text="Contraseña").grid(row=1, column=1, padx=10)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=2, column=1, padx=10)
    tk.Label(root, text="Nombre").grid(row=3, column=0, padx=10)
    name_entry = tk.Entry(root)
    name_entry.grid(row=4, column=0, padx=10)
    tk.Label(root, text="Dirección").grid(row=3, column=1, padx=10)
    address_entry = tk.Entry(root)
    address_entry.grid(row=4, column=1, padx=10)
    tk.Label(root, text="Teléfono").grid(row=3, column=2, padx=10)
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=4, column=2, padx=10)
    tk.Label(root, text="Email").grid(row=3, column=3, padx=10)
    email_entry = tk.Entry(root)
    email_entry.grid(row=4, column=3, padx=10)

    # Botones para registrar e iniciar sesión
    register_button = tk.Button(root, text="Registrar", command=register_user)
    register_button.grid(row=5, column=0, columnspan=2, pady=10)

    login_button = tk.Button(root, text="Iniciar Sesión", command=login)
    login_button.grid(row=5, column=2, columnspan=2, pady=10)

    root.mainloop()

