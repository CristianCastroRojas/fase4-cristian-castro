from config.constantes_globales import (TITULO_APP, NOMBRE_ESTUDIANTE, CLAVE_ACCESO)
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from config.constantes_login import (
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_BLANCO,
    COLOR_ERROR,
    COLOR_BORDE,
    COLOR_TEXTO_SECUNDARIO,
    FUENTE_TITULO,
    FUENTE_NORMAL,
    FUENTE_BOTON,
    FUENTE_FOOTER,
    TEXTO_CREDENCIAL,
    TEXTO_BOTON_LOGIN,
    TEXTO_BOTON_SALIR,
    TEXTO_FOOTER,
    MENSAJE_ERROR_VACIO,
    MENSAJE_ERROR_CLAVE,
    MENSAJE_ACCESO_OK,
    ANCHO_VENTANA,
    ALTO_VENTANA,
    ANCHO_FRAME,
    ALTO_FRAME
)


class LoginApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title(f"Acceso - {TITULO_APP}")
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg=COLOR_FONDO)

        self.crear_interfaz()
        self.centrar()

    # =========================
    # CENTRAR VENTANA
    # =========================
    def centrar(self):
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (ANCHO_VENTANA // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (ALTO_VENTANA // 2)
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}+{x}+{y}")

    # =========================
    # INTERFAZ
    # =========================
    def crear_interfaz(self):

        frame = tk.Frame(
            self.ventana,
            bg=COLOR_BLANCO,
            highlightthickness=1,
            highlightbackground=COLOR_BORDE
        )
        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=ANCHO_FRAME,
            height=ALTO_FRAME
        )

        # =========================
        # TÍTULO
        # =========================
        tk.Label(
            frame,
            text=TITULO_APP,
            font=FUENTE_TITULO,
            bg=COLOR_BLANCO,
            fg=COLOR_PRIMARIO
        ).pack(pady=10)

        # =========================
        # INFO
        # =========================
        tk.Label(
            frame,
            text=f"Estudiante: {NOMBRE_ESTUDIANTE}",
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO
        ).pack()

        tk.Label(
            frame,
            text=f"Fecha: {datetime.now().strftime('%d/%m/%Y')}",
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO
        ).pack()

        # =========================
        # INPUT
        # =========================
        tk.Label(
            frame,
            text=TEXTO_CREDENCIAL,
            font=FUENTE_NORMAL,
            bg=COLOR_BLANCO
        ).pack(pady=(10, 0))

        self.entry = tk.Entry(frame, show="*", font=FUENTE_NORMAL)
        self.entry.pack(pady=5)
        self.entry.focus()

        self.entry.bind("<Return>", lambda e: self.validar())

        # =========================
        # BOTONES
        # =========================
        btn_frame = tk.Frame(frame, bg=COLOR_BLANCO)
        btn_frame.pack(pady=15, fill="x", padx=20)

        tk.Button(
            btn_frame,
            text=TEXTO_BOTON_LOGIN,
            command=self.validar,
            bg=COLOR_PRIMARIO,
            fg="white",
            font=FUENTE_BOTON,
            bd=0,
            height=2
        ).pack(side="left", expand=True, fill="x", padx=5)

        tk.Button(
            btn_frame,
            text=TEXTO_BOTON_SALIR,
            command=self.ventana.destroy,
            bg=COLOR_ERROR,
            fg="white",
            font=FUENTE_BOTON,
            bd=0,
            height=2
        ).pack(side="left", expand=True, fill="x", padx=5)

        # =========================
        # FOOTER
        # =========================
        tk.Label(
            self.ventana,
            text=TEXTO_FOOTER,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_FOOTER
        ).pack(side="bottom", pady=10)

    # =========================
    # VALIDACIÓN
    # =========================
    def validar(self):
        clave = self.entry.get()

        if clave.strip() == "":
            messagebox.showerror("Error", MENSAJE_ERROR_VACIO)
            return

        if clave != CLAVE_ACCESO:
            messagebox.showerror("Error", MENSAJE_ERROR_CLAVE)
            self.entry.delete(0, tk.END)
            return

        messagebox.showinfo("Acceso correcto", MENSAJE_ACCESO_OK)

        self.ventana.destroy()

        import interfaz_principal
        interfaz_principal.iniciar_app()

    # =========================
    # EJECUTAR
    # =========================
    def ejecutar(self):
        self.ventana.mainloop()