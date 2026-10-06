"""Lista enlazada simple implementada desde cero.

No usa las listas nativas de Python como base interna.

Avance 1 — INF-220 Estructuras de Datos I

Complejidad temporal de las operaciones:
    insertar_inicio(dato)  -> O(1)
    insertar_final(dato)   -> O(n)   recorre hasta el último nodo
    buscar(dato)           -> O(n)
    eliminar(dato)         -> O(n)
    tamanio()              -> O(1)   se mantiene un contador
"""

from estructuras.nodo import Nodo


class ListaEnlazada:
    """Lista enlazada simple de nodos con cabeza y contador de tamaño."""

    def __init__(self):
        self._cabeza: Nodo | None = None
        self._tamanio = 0

    # ------------------------------------------------------------------
    # Consultas básicas
    # ------------------------------------------------------------------
    def esta_vacia(self) -> bool:
        """Devuelve True si la lista no contiene nodos. Complejidad: O(1)."""
        return self._cabeza is None

    def tamanio(self) -> int:
        """Cantidad de elementos. Complejidad: O(1)."""
        return self._tamanio

    # ------------------------------------------------------------------
    # Inserción
    # ------------------------------------------------------------------
    def insertar_inicio(self, dato) -> None:
        """Inserta un dato al inicio de la lista. Complejidad: O(1)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self._cabeza
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_final(self, dato) -> None:
        """Inserta un dato al final de la lista. Complejidad: O(n)."""
        nuevo = Nodo(dato)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    # ------------------------------------------------------------------
    # Búsqueda y eliminación
    # ------------------------------------------------------------------
    def buscar(self, dato):
        """Devuelve el primer nodo cuyo dato coincida, o None. O(n)."""
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_inicio(self):
        """Elimina y devuelve el primer dato. Complejidad: O(1).

        Lanza ValueError si la lista está vacía.
        """
        if self._cabeza is None:
            raise ValueError("No se puede eliminar: la lista está vacía")
        dato = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato

    def eliminar(self, dato) -> bool:
        """Elimina la primera aparición de un dato. Complejidad: O(n)."""
        if self._cabeza is None:
            return False
        if self._cabeza.dato == dato:
            self.eliminar_inicio()
            return True
        anterior = self._cabeza
        actual = self._cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    # ------------------------------------------------------------------
    # Recorrido
    # ------------------------------------------------------------------
    def a_lista(self) -> list:
        """Convierte la lista enlazada en una lista nativa (solo para mostrar
        en la interfaz). Recorrido completo: O(n)."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __iter__(self):
        """Permite recorrer la lista con for dato in lista. O(n)."""
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        elementos = " -> ".join(str(d) for d in self)
        return f"[{elementos}] -> None" if elementos else "None"
