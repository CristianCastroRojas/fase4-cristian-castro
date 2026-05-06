from config.constantes_globales import (TITULO_APP, NOMBRE_ESTUDIANTE)
import tkinter as tk
from tkinter import messagebox

from arbol import ArbolBinarioBusqueda
from renderizador import RenderizadorArbol

from config.constantes_interfaz import (
    ANCHO_VENTANA,
    ALTO_VENTANA,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_EXITO,
    COLOR_PELIGRO,
    COLOR_BLANCO,
    COLOR_CANVAS_BORDE,
    TEXTO_INPUT,
    TEXTO_PREORDEN,
    TEXTO_INORDEN,
    TEXTO_POSORDEN,
    ERROR_VACIO,
    ERROR_SOLO_ENTEROS,
    ERROR_GENERAL,
    MSG_EXISTE,
    MSG_NO_EXISTE
)


def iniciar_app():
    Ventana()


class Ventana:
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda()

        self.ventana = tk.Tk()
        self.ventana.title(TITULO_APP + " - " + NOMBRE_ESTUDIANTE)
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.resizable(False, False)

        self.ventana.configure(bg=COLOR_FONDO)

        self.ultimo_agregado = None

        self.crear_interfaz()
        self.ventana.mainloop()

    # =========================
    # INTERFAZ
    # =========================
    def crear_interfaz(self):

        header = tk.Frame(self.ventana, bg=COLOR_PRIMARIO, height=60)
        header.pack(fill="x")

        tk.Label(
            header,
            text=TITULO_APP.upper(),
            bg=COLOR_PRIMARIO,
            fg="white",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=15)

        main_frame = tk.Frame(self.ventana, bg=COLOR_FONDO)
        main_frame.pack(fill="both", expand=True, padx=25, pady=15)

        form = tk.Frame(main_frame, bg=COLOR_BLANCO)
        form.pack(pady=(0, 10), fill="x")

        tk.Label(
            form,
            text=TEXTO_INPUT,
            bg=COLOR_BLANCO,
            font=("Segoe UI", 10)
        ).pack(anchor="w")

        self.entry = tk.Entry(form, font=("Segoe UI", 12))
        self.entry.pack(fill="x", pady=5)
        self.entry.focus()

        btn_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=10, fill="x")

        tk.Button(
            btn_frame,
            text="AGREGAR NODO",
            bg=COLOR_PRIMARIO,
            fg="white",
            command=self.agregar,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        tk.Button(
            btn_frame,
            text="BUSCAR NODO",
            bg=COLOR_EXITO,
            fg="white",
            command=self.buscar,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", expand=True, fill="x", padx=5)

        tk.Button(
            btn_frame,
            text="LIMPIAR",
            bg="#f0ad4e",
            fg="white",
            command=self.limpiar,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", expand=True, fill="x", padx=5)

        tk.Button(
            btn_frame,
            text="SALIR",
            bg=COLOR_PELIGRO,
            fg="white",
            command=self.ventana.destroy,
            font=("Segoe UI", 10, "bold")
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

        tk.Label(
            main_frame,
            text="ÁRBOL",
            bg=COLOR_FONDO,
            font=("Segoe UI", 12, "bold")
        ).pack(pady=(10, 0))

        self.canvas = tk.Canvas(
            main_frame,
            width=850,
            height=280,
            bg="white",
            highlightthickness=1,
            highlightbackground=COLOR_CANVAS_BORDE
        )
        self.canvas.pack(pady=10)

        # Aplicación del Principio de Responsabilidad Única (SRP - SOLID)
        self.renderizador = RenderizadorArbol(self.canvas)

        rec_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        rec_frame.pack(pady=5)

        tk.Label(rec_frame, text=TEXTO_PREORDEN, bg=COLOR_FONDO).grid(row=0, column=0)
        tk.Label(rec_frame, text=TEXTO_INORDEN, bg=COLOR_FONDO).grid(row=0, column=1)
        tk.Label(rec_frame, text=TEXTO_POSORDEN, bg=COLOR_FONDO).grid(row=0, column=2)

        self.pre = tk.Text(rec_frame, height=4, width=30)
        self.ino = tk.Text(rec_frame, height=4, width=30)
        self.pos = tk.Text(rec_frame, height=4, width=30)

        # Configurar para centrar el texto
        self.pre.tag_configure("center", justify="center")
        self.ino.tag_configure("center", justify="center")
        self.pos.tag_configure("center", justify="center")

        # Configurar como solo lectura
        self.pre.config(state=tk.DISABLED, bg="#f0f0f0")
        self.ino.config(state=tk.DISABLED, bg="#f0f0f0")
        self.pos.config(state=tk.DISABLED, bg="#f0f0f0")

        self.pre.grid(row=1, column=0, padx=5)
        self.ino.grid(row=1, column=1, padx=5)
        self.pos.grid(row=1, column=2, padx=5)

    # =========================
    # VALIDACIÓN
    # =========================
    def validar(self):
        v = self.entry.get()

        if v.strip() == "":
            messagebox.showerror(ERROR_GENERAL, ERROR_VACIO)
            return None

        if not v.isdigit():
            messagebox.showerror(ERROR_GENERAL, ERROR_SOLO_ENTEROS)
            return None

        return int(v)

    # =========================
    # AGREGAR
    # =========================
    def agregar(self):
        v = self.validar()
        if v is None:
            return

        try:
            self.arbol.insertar(v)
            self.ultimo_agregado = v
            self.actualizar()
            self.entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror(ERROR_GENERAL, str(e))

    # =========================
    # BUSCAR
    # =========================
    def buscar(self):
        v = self.validar()
        if v is None:
            return

        if self.arbol.buscar(v):
            messagebox.showinfo("Resultado", MSG_EXISTE.format(valor=v))
        else:
            messagebox.showwarning("Resultado", MSG_NO_EXISTE.format(valor=v))

    # =========================
    # LIMPIAR
    # =========================
    def limpiar(self):
        self.arbol.limpiar()
        self.ultimo_agregado = None
        self.actualizar()
        self.canvas.delete("all")

    # =========================
    # ACTUALIZAR
    # =========================
    def actualizar(self):
        self.pre.config(state=tk.NORMAL)
        self.ino.config(state=tk.NORMAL)
        self.pos.config(state=tk.NORMAL)

        self.pre.delete("1.0", tk.END)
        self.ino.delete("1.0", tk.END)
        self.pos.delete("1.0", tk.END)

        str_pre = ", ".join(map(str, self.arbol.preorden()))
        str_ino = ", ".join(map(str, self.arbol.inorden()))
        str_pos = ", ".join(map(str, self.arbol.posorden()))

        self.pre.insert(tk.END, str_pre, "center")
        self.ino.insert(tk.END, str_ino, "center")
        self.pos.insert(tk.END, str_pos, "center")

        self.pre.config(state=tk.DISABLED)
        self.ino.config(state=tk.DISABLED)
        self.pos.config(state=tk.DISABLED)

        self.renderizador.dibujar(self.arbol, self.ultimo_agregado)