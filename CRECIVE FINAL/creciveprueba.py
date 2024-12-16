import tkinter as tk
from tkinter import messagebox
import csv
from tkinter import ttk
import os
from tkinter import PhotoImage

# ---------------------- CONFIGURACIONES GENERALES ----------------------
COLOR_FONDO = "#EFE5D5"  # Color de fondo
COLOR_BOTON = "#A6B49B"  # Color de los botones
COLOR_TEXTO = "#3C3C3C"  # Color del texto
COLOR_TEXTO_BOTON = "#FFFFFF"  # Color del texto de los botones
FUENTE_TITULO = ("Arial", 18, "bold")
FUENTE_TEXTO = ("Arial", 12)
FUENTE_BOTON = ("Arial", 12, "bold")
FUENTE_USUARIO = ("Arial", 14, "bold")

# Variables globales
usuario_actual = None
historial_calculos = "historial.csv"
usuarios_archivo = "usuarios.csv"

# ---------------------- FUNCIONES DE INTERFAZ ----------------------

def mostrar_introduccion(root):
    # Pantalla combinada de Introducción e Inicio de Sesión
    frame_intro_sesion = tk.Frame(root, bg=COLOR_FONDO)
    frame_intro_sesion.pack(fill="both", expand=True)

    # Texto introductorio
    texto_intro = """Bienvenidos! Este programa ayudará a la producción de velas y jabones, orientado al cálculo de su producción.
Este software se convierte en su aliado esencial para reducir el impacto ambiental de sus procesos productivos."""
    
    label_intro = tk.Label(frame_intro_sesion, text=texto_intro, font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO, wraplength=700)
    label_intro.pack(padx=20, pady=50)

    # Campos de usuario y contraseña
    label_usuario = tk.Label(frame_intro_sesion, text="Ingrese su nombre de usuario", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_usuario.pack(pady=20)

    entrada_usuario = tk.Entry(frame_intro_sesion, font=FUENTE_TEXTO)
    entrada_usuario.pack(pady=10)

    label_contrasena = tk.Label(frame_intro_sesion, text="Ingrese su contraseña", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_contrasena.pack(pady=10)

    entrada_contrasena = tk.Entry(frame_intro_sesion, show="*", font=FUENTE_TEXTO)
    entrada_contrasena.pack(pady=10)

    # Botón para iniciar sesión
    boton_ingresar = tk.Button(
        frame_intro_sesion, text="Iniciar sesión", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON,
        command=lambda: verificar_credenciales(root, frame_intro_sesion, entrada_usuario.get(), entrada_contrasena.get())
    )
    boton_ingresar.pack(pady=20)

def verificar_credenciales(root, frame_anterior, usuario, contrasena):
    if not os.path.exists(usuarios_archivo):
        with open(usuarios_archivo, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["admin", "admin"])  # Crear un usuario admin predeterminado

    with open(usuarios_archivo, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == usuario and row[1] == contrasena:
                mostrar_menu_calculos(root, frame_anterior, usuario)
                return

    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def mostrar_menu_calculos(root, frame_anterior, usuario):
    global usuario_actual
    usuario_actual = usuario  # Guardamos el usuario actual

    frame_anterior.pack_forget()  # Ocultamos la pantalla anterior

    # Pantalla de menú
    frame_menu = tk.Frame(root, bg=COLOR_FONDO)
    frame_menu.pack(fill="both", expand=True)

        # Contenedor para los botones
    frame_botones = tk.Frame(frame_menu, bg=COLOR_FONDO)
    frame_botones.pack(pady=20)

    # Dimensiones uniformes de los botones
    boton_ancho = 20
    boton_alto = 2

    # Opciones de acción
    boton_calculos = tk.Button(frame_menu, text="Hacer Cálculos", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON,width=boton_ancho,height=boton_alto, command=lambda: mostrar_calculadora(root, frame_menu))
    boton_calculos.pack(pady=20)

    boton_historico = tk.Button(frame_menu, text="Historial", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON,width=boton_ancho,height=boton_alto,  command=lambda: mostrar_historial(root, frame_menu))
    boton_historico.pack(pady=20)

        # Botón Salir
    boton_salir = tk.Button(frame_botones, text="Salir", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, width=boton_ancho, height=boton_alto, command=root.destroy)
    boton_salir.grid(row=2, column=0, padx=10, pady=5)

    if usuario == "admin":
        boton_registrar_usuario = tk.Button(frame_menu, text="Registrar Usuario", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON,width=boton_ancho,height=boton_alto,  command=lambda: registrar_usuario(root, frame_menu))
        boton_registrar_usuario.pack(pady=20)

def mostrar_calculadora(root, frame_anterior):
    frame_anterior.pack_forget()  # Ocultamos la pantalla anterior

    # Pantalla de cálculos
    frame_calculos = tk.Frame(root, bg=COLOR_FONDO)
    frame_calculos.pack(fill="both", expand=True)

    # Título de cálculos
    label_calculos = tk.Label(frame_calculos, text="Calculadora de Producción", font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_calculos.pack(pady=20)

    # Panel izquierdo con opciones de cálculo
    frame_left = tk.Frame(frame_calculos, bg=COLOR_FONDO)
    frame_left.pack(side="left", padx=50, pady=50)

    # Opciones de cálculo (botones verdes)
    label_opciones = tk.Label(frame_left, text="Seleccione el tipo de cálculo", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_opciones.pack(pady=10)

    boton_aceite_a_vela = tk.Button(frame_left, text="Aceite a Vela", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Aceite a Vela"))
    boton_aceite_a_vela.pack(pady=10)

    boton_vela_a_aceite = tk.Button(frame_left, text="Vela a Aceite", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Vela a Aceite"))
    boton_vela_a_aceite.pack(pady=10)

    boton_jabon_a_aceite = tk.Button(frame_left, text="Jabón a Aceite", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Jabón a Aceite"))
    boton_jabon_a_aceite.pack(pady=10)

    boton_aceite_a_jabon = tk.Button(frame_left, text="Aceite a Jabón", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Aceite a Jabón"))
    boton_aceite_a_jabon.pack(pady=10)

    # Panel derecho con opción de unidades y campos de cantidad
    frame_right = tk.Frame(frame_calculos, bg=COLOR_FONDO)
    frame_right.pack(side="right", padx=50, pady=50)

    # Etiqueta de la selección
    global label_seleccion_transformacion
    label_seleccion_transformacion = tk.Label(frame_right, text="Selecciona una transformación", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_seleccion_transformacion.pack(pady=20)

    # Entrada para cantidad
    label_cantidad = tk.Label(frame_right, text="Ingrese la cantidad", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_cantidad.pack(pady=10)

    entrada_cantidad = tk.Entry(frame_right, font=FUENTE_TEXTO)
    entrada_cantidad.pack(pady=10)

    # Unidades según el tipo de transformación (Combobox)
    label_unidad = tk.Label(frame_right, text="Seleccionar unidad", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_unidad.pack(pady=10)

    unidades = ["Litros", "Mililitros", "Gramos", "Kilos"]
    combo_unidades = ttk.Combobox(frame_right, values=unidades, font=FUENTE_TEXTO)
    combo_unidades.set("Mililitros")  # Por defecto, Mililitros
    combo_unidades.pack(pady=10)

    # Mostrar cantidad mínima para transformación
    global label_minima
    label_minima = tk.Label(frame_right, text="Cantidad mínima: ", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_minima.pack(pady=10)

    # Botón de regresar (corrected)
    boton_regresar = tk.Button(frame_right, text="Regresar", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: mostrar_menu_calculos(root, frame_calculos, usuario_actual))
    boton_regresar.pack(pady=10)

    # Botón de cálculo
    boton_calcular = tk.Button(frame_right, text="Calcular", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: realizar_calculo(entrada_cantidad.get(), combo_unidades.get()))
    boton_calcular.pack(pady=20)

    # Resultado
    global label_resultado
    label_resultado = tk.Label(frame_right, text="Lo que obtendrás: ", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_resultado.pack(pady=20)

    # Botón de guardar historial
    boton_guardar_historial = tk.Button(frame_right, text="Guardar Historial", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=guardar_historial)
    boton_guardar_historial.pack(pady=10)

# ---------------------- FUNCIONES DE ORDENAMIENTO ----------------------

def quick_merge_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]  # Usamos el elemento del medio como pivote
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_merge_sort(left) + middle + quick_merge_sort(right)

def cargar_historial_ordenado():
    datos = []
    if os.path.exists(historial_calculos):
        with open(historial_calculos, mode="r") as file:
            reader = csv.reader(file)
            datos = list(reader)
    
    # Ordenamos por el segundo elemento (tipo de cálculo)
    datos_ordenados = quick_merge_sort(datos)
    return datos_ordenados
# ---------------------- FUNCIONES DE REGISTRO ----------------------

def registrar_usuario(root, frame_anterior):
    frame_anterior.pack_forget()

    frame_registro = tk.Frame(root, bg=COLOR_FONDO)
    frame_registro.pack(fill="both", expand=True)

    label_titulo = tk.Label(frame_registro, text="Registrar Nuevo Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_titulo.pack(pady=20)

    label_usuario = tk.Label(frame_registro, text="Nombre de Usuario", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_usuario.pack(pady=10)

    entrada_usuario = tk.Entry(frame_registro, font=FUENTE_TEXTO)
    entrada_usuario.pack(pady=10)

    label_contrasena = tk.Label(frame_registro, text="Contraseña", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_contrasena.pack(pady=10)

    entrada_contrasena = tk.Entry(frame_registro, font=FUENTE_TEXTO)
    entrada_contrasena.pack(pady=10)

    boton_registrar = tk.Button(
        frame_registro, text="Registrar", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON,
        command=lambda: guardar_usuario(entrada_usuario.get(), entrada_contrasena.get())
    )
    boton_registrar.pack(pady=20)

    boton_regresar = tk.Button(frame_registro, text="Regresar", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: mostrar_menu_calculos(root, frame_registro, usuario_actual))
    boton_regresar.pack(pady=10)

def guardar_usuario(usuario, contrasena):
    if not usuario or not contrasena:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    with open(usuarios_archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([usuario, contrasena])
    
    messagebox.showinfo("Éxito", "Usuario registrado correctamente")

def guardar_historial():
    # Verificar que se haya realizado un cálculo
    if label_seleccion_transformacion.cget("text") == "Selecciona una transformación":
        messagebox.showerror("Error", "Primero debe realizar un cálculo")
        return

    # Obtener los detalles del cálculo
    transformacion = label_seleccion_transformacion.cget("text").replace("Seleccionado: ", "")
    resultado = label_resultado.cget("text").replace("Lo que obtendrás: ", "")

    # Guardar en el archivo CSV
    with open(historial_calculos, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([usuario_actual, transformacion, resultado])

    messagebox.showinfo("Éxito", "Cálculo guardado en el historial")

# ---------------------- FUNCIONES DE CALCULO ----------------------
def mostrar_calculadora(root, frame_anterior):
    frame_anterior.pack_forget()  # Ocultamos la pantalla anterior

    # Pantalla de cálculos
    frame_calculos = tk.Frame(root, bg=COLOR_FONDO)
    frame_calculos.pack(fill="both", expand=True)

    # Título de cálculos
    label_calculos = tk.Label(frame_calculos, text="Calculadora de Producción", font=("Arial", 24, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_calculos.pack(pady=20)

    # Panel izquierdo con opciones de cálculo
    frame_left = tk.Frame(frame_calculos, bg=COLOR_FONDO)
    frame_left.pack(side="left", padx=50, pady=50)

    # Opciones de cálculo (botones verdes)
    label_opciones = tk.Label(frame_left, text="Seleccione el tipo de cálculo", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_opciones.pack(pady=10)

    boton_aceite_a_vela = tk.Button(frame_left, text="Aceite a Vela", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Aceite a Vela"))
    boton_aceite_a_vela.pack(pady=10)

    boton_vela_a_aceite = tk.Button(frame_left, text="Vela a Aceite", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Vela a Aceite"))
    boton_vela_a_aceite.pack(pady=10)

    boton_jabon_a_aceite = tk.Button(frame_left, text="Jabón a Aceite", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Jabón a Aceite"))
    boton_jabon_a_aceite.pack(pady=10)

    boton_aceite_a_jabon = tk.Button(frame_left, text="Aceite a Jabón", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: seleccionar_transformacion("Aceite a Jabón"))
    boton_aceite_a_jabon.pack(pady=10)

    # Panel derecho con opción de unidades y campos de cantidad
    frame_right = tk.Frame(frame_calculos, bg=COLOR_FONDO)
    frame_right.pack(side="right", padx=50, pady=50)

    # Etiqueta de la selección
    global label_seleccion_transformacion
    label_seleccion_transformacion = tk.Label(frame_right, text="Selecciona una transformación", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_seleccion_transformacion.pack(pady=20)

    # Entrada para cantidad
    label_cantidad = tk.Label(frame_right, text="Ingrese la cantidad", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_cantidad.pack(pady=10)

    entrada_cantidad = tk.Entry(frame_right, font=FUENTE_TEXTO)
    entrada_cantidad.pack(pady=10)

    # Unidades según el tipo de transformación (Combobox)
    label_unidad = tk.Label(frame_right, text="Seleccionar unidad", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_unidad.pack(pady=10)

    unidades = ["Mililitros", "Gramos"]
    combo_unidades = ttk.Combobox(frame_right, values=unidades, font=FUENTE_TEXTO)
    combo_unidades.set("Mililitros")  # Por defecto, Mililitros
    combo_unidades.pack(pady=10)

    # Botón de cálculo
    boton_calcular = tk.Button(frame_right, text="Calcular", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: realizar_calculo(entrada_cantidad.get(), combo_unidades.get()))
    boton_calcular.pack(pady=20)

    # Resultado
    global label_resultado
    label_resultado = tk.Label(frame_right, text="Lo que obtendrás: ", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_resultado.pack(pady=20)

    # Botón de regresar (corrected)
    boton_regresar = tk.Button(frame_right, text="Regresar", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: mostrar_menu_calculos(root, frame_calculos, usuario_actual))
    boton_regresar.pack(pady=10)


    # Botón de guardar historial
    boton_guardar_historial = tk.Button(frame_right, text="Guardar Historial", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=guardar_historial)
    boton_guardar_historial.pack(pady=10)

def seleccionar_transformacion(transformacion):
    label_seleccion_transformacion.config(text=f"Seleccionado: {transformacion}")

def convertir_a_unidad_base(cantidad, unidad):
    # Si la unidad seleccionada es Mililitros, convertir a Gramos
    if unidad == "Mililitros":
        return cantidad  # En este caso, 1 ml = 1 gramo para esta conversión simplificada
    elif unidad == "Gramos":
        return cantidad  # 1 gramo es igual a 1 gramo en este caso también
    return cantidad

def realizar_calculo(cantidad_str, unidad):
    try:
        cantidad = float(cantidad_str)  # Convertir a float, se puede poner un chequeo más estricto si se desea
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad numérica válida.")
        return

    # Convertir a la unidad base (gramos o mililitros)
    cantidad_convertida = convertir_a_unidad_base(cantidad, unidad)

    # Fórmulas de cálculo (ajustar según el tipo de transformación)
    if label_seleccion_transformacion.cget("text") == "Seleccionado: Aceite a Vela":
        resultado = cantidad_convertida / 100  # Fórmula para calcular el número de velas
        unidad_resultado = "velas"
    elif label_seleccion_transformacion.cget("text") == "Seleccionado: Vela a Aceite":
        resultado = cantidad_convertida * 100  # Fórmula para calcular ml de aceite necesarios
        unidad_resultado = "mililitros de aceite"
    elif label_seleccion_transformacion.cget("text") == "Seleccionado: Jabón a Aceite":
        resultado = cantidad_convertida * 50  # Fórmula para calcular ml de aceite necesarios para jabones
        unidad_resultado = "mililitros de aceite"
    elif label_seleccion_transformacion.cget("text") == "Seleccionado: Aceite a Jabón":
        resultado = cantidad_convertida / 50  # Fórmula para calcular el número de jabones
        unidad_resultado = "jabones"

    # Mostrar el resultado
    label_resultado.config(text=f"Lo que obtendrás: {int(resultado)} {unidad_resultado}")
    messagebox.showinfo("Cálculo realizado", f"Resultado: {int(resultado)} {unidad_resultado}")

def mostrar_historial(root, frame_anterior):
    frame_anterior.pack_forget()  # Ocultamos la pantalla anterior

    # Crear frame para el historial
    frame_historial = tk.Frame(root, bg=COLOR_FONDO)
    frame_historial.pack(fill="both", expand=True)

    # Título del historial
    label_historial = tk.Label(frame_historial, text="Historial de Cálculos", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO)
    label_historial.pack(pady=20)

    # Frame para la tabla y botones
    frame_tabla = tk.Frame(frame_historial, bg="white")
    frame_tabla.pack(padx=50, pady=20, fill="both", expand=True)

    # Crear Treeview
    columns = ("Usuario", "Tipo de Cálculo", "Cantidad")
    tabla_historial = ttk.Treeview(frame_tabla, columns=columns, show="headings")
    
    # Definir encabezados de la tabla
    tabla_historial.heading("Usuario", text="Usuario")
    tabla_historial.heading("Tipo de Cálculo", text="Tipo de Cálculo")
    tabla_historial.heading("Cantidad", text="Cantidad")
    
    tabla_historial.pack(fill="both", expand=True)

    # Cargar datos del historial desde el archivo CSV y ordenarlos
    datos_ordenados = cargar_historial_ordenado()
    for row in datos_ordenados:
        tabla_historial.insert("", "end", values=row)
    
    # Botón para regresar
    boton_regresar = tk.Button(frame_historial, text="Regresar", font=FUENTE_BOTON, bg=COLOR_BOTON, fg=COLOR_TEXTO_BOTON, command=lambda: mostrar_menu_calculos(root, frame_historial, usuario_actual))
    boton_regresar.pack(pady=20)

# Ejecutar la aplicación
root = tk.Tk()
root.title("Crecive")
root.geometry("900x600")
root.config(bg=COLOR_FONDO)

mostrar_introduccion(root)

root.mainloop()