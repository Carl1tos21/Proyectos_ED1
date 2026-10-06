"""Lista doblemente enlazada — IMPLEMENTACIÓN PARCIAL (Avance 1).

Avance 1 — INF-220 Estructuras de Datos I

En este primer avance solo se implementan las insercciones y los
recorridos bidireccional. Las operaciones de eliminación y búsqueda
quedan PENDIENTES para el próximo avance.

Pendiente:
    - eliminar_final()   -> O(1)  ← ventaja de la lista doble
    - eliminar(dato)     -> O(n)
    - buscar(dato)       -> O(n)
"""

from estructuras.nodo import NodoDoble


class ListaDoble:
    """Lista doblemente enlazada con cabeza, cola y contador de tamaño."""

    def __init__(self):
        self._cabeza: NodoDoble | None = None
        self._cola: NodoDoble | None = None
        self._tamanio = 0

    # ------------------------------------------------------------------
    # Consultas básicas
    # ------------------------------------------------------------------
    def esta_vacia(self) -> bool:
        """Complejidad: O(1)."""
        return self._cabeza is None

    def tamanio(self) -> int:
        """Complejidad: O(1)."""
        return self._tamanio

    # ------------------------------------------------------------------
    # Inserción (avance 1)
    # ------------------------------------------------------------------
    def insertar_inicio(self, dato) -> None:
        """Inserta al inicio. Complejidad: O(1)."""
        nuevo = NodoDoble(dato)
        if self._cabeza is None:
            self._cabeza = self._cola = nuevo
        else:
            nuevo.siguiente = self._cabeza
            self._cabeza.anterior = nuevo
            self._cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato) -> None:
        """Inserta al final. Complejidad: O(1) por la referencia a cola."""
        nuevo = NodoDoble(dato)
        if self._cola is None:
            self._cabeza = self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamanio += 1

    # ------------------------------------------------------------------
    # Recorrido bidireccional (avance 1)
    # ------------------------------------------------------------------
    def a_lista_adelante(self) -> list:
        """Recorrido cabeza -> cola. O(n)."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def a_lista_atras(self) -> list:
        """Recorrido cola -> cabeza. O(n)."""
        resultado = []
        actual = self._cola
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.anterior
        return resultado

    # ------------------------------------------------------------------
    # PENDIENTES PARA EL PRÓXIMO AVANCE
    # ------------------------------------------------------------------
    def eliminar_final(self):
        raise NotImplementedError(
            "Pendiente: eliminar_final() en el próximo avance")

    def eliminar(self, dato):
        raise NotImplementedError(
            "Pendiente: eliminar(dato) en el próximo avance")

    def buscar(self, dato):
        raise NotImplementedError(
            "Pendiente: buscar(dato) en el próximo avance")

    def __str__(self):
        elementos = " <-> ".join(str(d) for d in self.a_lista_adelante())
        return f"[{elementos}]" if elementos else "[]"
