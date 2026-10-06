"""Pila (Stack) LIFO implementada desde cero con nodos enlazados.

Avance 1 — INF-220 Estructuras de Datos I

El inicio de la lista ES el tope de la pila, por lo que todas las
operaciones principales son O(1):

    apilar(dato)   -> O(1)   (push)
    desapilar()    -> O(1)   (pop)
    cima()         -> O(1)   (peek)
    esta_vacia()   -> O(1)

Uso en el simulador: historial de acciones para Deshacer/Rehacer
(en el avance 1 solo Deshacer; el Rehacer con doble pila queda
PENDIENTE para el próximo avance).
"""

from estructuras.nodo import Nodo


class Pila:
    """Pila LIFO dinámica: el tope es la cabeza de la lista enlazada."""

    def __init__(self):
        self._tope: Nodo | None = None
        self._tamanio = 0

    def esta_vacia(self) -> bool:
        """Complejidad: O(1)."""
        return self._tope is None

    def tamanio(self) -> int:
        """Complejidad: O(1)."""
        return self._tamanio

    def apilar(self, dato) -> None:
        """Inserta un dato en el tope de la pila. Complejidad: O(1)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo
        self._tamanio += 1

    def desapilar(self):
        """Elimina y devuelve el dato del tope. Complejidad: O(1).

        Lanza ValueError si la pila está vacía.
        """
        if self._tope is None:
            raise ValueError("No se puede desapilar: la pila está vacía")
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._tamanio -= 1
        return dato

    def cima(self):
        """Devuelve el dato del tope sin quitarlo. Complejidad: O(1).

        Lanza ValueError si la pila está vacía.
        """
        if self._tope is None:
            raise ValueError("No hay cima: la pila está vacía")
        return self._tope.dato

    def a_lista(self) -> list:
        """Convierte la pila en lista nativa (tope al inicio). O(n)."""
        resultado = []
        actual = self._tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __iter__(self):
        """Itera desde el tope hacia el fondo. O(n)."""
        actual = self._tope
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        elementos = ", ".join(str(d) for d in self)
        return f"[{elementos}]" if elementos else "[]"
