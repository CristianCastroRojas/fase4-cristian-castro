import tkinter as tk
from config.constantes_interfaz import (
    COLOR_LINEA,
    COLOR_NIVEL_1,
    COLOR_NIVEL_2,
    COLOR_NIVEL_3,
    COLOR_NIVEL_4,
    COLOR_NIVEL_DEFAULT,
    COLOR_BORDE_NUEVO
)

class RenderizadorArbol:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ultimo_agregado = None

    def dibujar(self, arbol, ultimo_agregado=None):
        self.ultimo_agregado = ultimo_agregado
        self.canvas.delete("all")

        if arbol.raiz:
            self._dibujar_conexiones(arbol.raiz, 0, 850, 35)
            self._dibujar_nodos(arbol.raiz, 0, 850, 35)

    def _color_nivel(self, nivel):
        return {
            1: COLOR_NIVEL_1,
            2: COLOR_NIVEL_2,
            3: COLOR_NIVEL_3,
            4: COLOR_NIVEL_4
        }.get(nivel, COLOR_NIVEL_DEFAULT)

    def _dibujar_conexiones(self, nodo, izq, der, y, nivel=1):
        if not nodo:
            return

        x = (izq + der) // 2
        y_next = y + 75

        if nodo.izquierda:
            x_hijo = (izq + x) // 2
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)
            self._dibujar_conexiones(nodo.izquierda, izq, x, y_next, nivel + 1)

        if nodo.derecha:
            x_hijo = (x + der) // 2
            self.canvas.create_line(x, y, x_hijo, y_next, fill=COLOR_LINEA)
            self._dibujar_conexiones(nodo.derecha, x, der, y_next, nivel + 1)

    def _dibujar_nodos(self, nodo, izq, der, y, nivel=1):
        if not nodo:
            return

        x = (izq + der) // 2
        r = 24

        color = self._color_nivel(nivel)

        es_nuevo = (self.ultimo_agregado == nodo.valor)

        if es_nuevo:
            self._animar_crecimiento(x, y, color, str(nodo.valor), nivel, 2)
        else:
            self.canvas.create_oval(
                x - r, y - r,
                x + r, y + r,
                fill=color,
                outline=color
            )

            self.canvas.create_text(
                x, y,
                text=f"{nodo.valor}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center"
            )

        self._dibujar_nodos(nodo.izquierda, izq, x, y + 75, nivel + 1)
        self._dibujar_nodos(nodo.derecha, x, der, y + 75, nivel + 1)

    def _animar_crecimiento(self, x, y, color, valor_texto, nivel, r_actual):
        tag = f"nodo_{valor_texto}"
        self.canvas.delete(tag)

        if r_actual <= 24:
            self.canvas.create_oval(
                x - r_actual, y - r_actual,
                x + r_actual, y + r_actual,
                fill=color,
                outline="white",
                width=2,
                tags=tag
            )

            self.canvas.after(
                15,
                self._animar_crecimiento,
                x, y, color, valor_texto, nivel, r_actual + 3
            )
        else:
            self.canvas.create_oval(
                x - 24, y - 24,
                x + 24, y + 24,
                fill=color,
                outline=COLOR_BORDE_NUEVO,
                width=3,
                tags=tag
            )

            self.canvas.create_text(
                x, y,
                text=f"{valor_texto}\n(N{nivel})",
                fill="white",
                font=("Segoe UI", 8, "bold"),
                justify="center",
                tags=tag
            )
