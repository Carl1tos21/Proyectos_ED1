"""Nodos utilizados por las estructuras de datos del simulador.

Avance 1 — INF-220 Estructuras de Datos I
"""


class Nodo:
    """Nodo para lista enlazada simple.

    Contiene un dato y una referencia (puntero) al siguiente nodo.
    """

    def __init__(self, dato):
        self.dato = dato
        self.siguiente: "Nodo | None" = None

    def __repr__(self):
        return f"Nodo({self.dato!r})"


class NodoDoble:
    """Nodo para lista doblemente enlazada.

    Contiene un dato y referencias al siguiente y al anterior nodo.
    """

    def __init__(self, dato):
        self.dato = dato
        self.siguiente: "NodoDoble | None" = None
        self.anterior: "NodoDoble | None" = None

    def __repr__(self):
        return f"NodoDoble({self.dato!r})"
