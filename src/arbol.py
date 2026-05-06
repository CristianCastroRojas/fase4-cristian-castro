from config.constantes_arbol import (
    MAX_NIVELES,
    ERROR_MAX_NIVELES,
    ERROR_DUPLICADO
)


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # ============================
    # INSERTAR
    # ============================
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor, 1)

    def _insertar(self, nodo, valor, nivel):

        if nivel > MAX_NIVELES:
            raise Exception(ERROR_MAX_NIVELES)

        if nodo is None:
            return Nodo(valor)

        if valor == nodo.valor:
            raise Exception(ERROR_DUPLICADO)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor, nivel + 1)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor, nivel + 1)

        return nodo

    # ============================
    # BUSCAR
    # ============================
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    # ============================
    # RECORRIDOS
    # ============================
    def preorden(self):
        res = []
        self._pre(self.raiz, res)
        return res

    def _pre(self, nodo, res):
        if nodo:
            res.append(nodo.valor)
            self._pre(nodo.izquierda, res)
            self._pre(nodo.derecha, res)

    def inorden(self):
        res = []
        self._ino(self.raiz, res)
        return res

    def _ino(self, nodo, res):
        if nodo:
            self._ino(nodo.izquierda, res)
            res.append(nodo.valor)
            self._ino(nodo.derecha, res)

    def posorden(self):
        res = []
        self._pos(self.raiz, res)
        return res

    def _pos(self, nodo, res):
        if nodo:
            self._pos(nodo.izquierda, res)
            self._pos(nodo.derecha, res)
            res.append(nodo.valor)

    # ============================
    # LIMPIAR
    # ============================
    def limpiar(self):
        self.raiz = None