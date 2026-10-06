"""CentroLogistico — Modelo (M) del patrón MVC.

Avance 1 — INF-220 Estructuras de Datos I

Responsabilidades:
  - Guardar en memoria los paquetes registrados (lista enlazada simple).
  - Mantener el historial de acciones en una PILA para poder deshacer
    el último registro (avance 1: solo Deshacer; Rehacer PENDIENTE).

Este módulo NO importa Flet ni ningún componente de la interfaz.
"""

from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila
from modelo.paquete import Paquete


class CentroLogistico:
    """Modelo de datos del simulador de logística."""

    def __init__(self):
        self.paquetes = ListaEnlazada()      # inventario actual (lista simple)
        self.historial = Pila()              # acciones para Deshacer (LIFO)
        self._contador_id = 0                # correlativo de paquetes O(1)

    # ------------------------------------------------------------------
    # Operaciones del avance 1
    # ------------------------------------------------------------------
    def siguiente_id(self) -> int:
        """Devuelve el próximo id a asignar sin consumirlo. O(1)."""
        return self._contador_id + 1

    def registrar_paquete(self, destinatario: str, destino: str,
                          peso_kg: float,
                          prioridad: str = "Normal") -> Paquete:
        """Registra un paquete nuevo: lo agrega al inventario y empuja la
        acción en el historial (pila) para poder deshacerla.

        Complejidad: O(1) inserción al final de la lista + O(1) apilado.
        """
        if not destinatario.strip():
            raise ValueError("El destinatario es obligatorio")
        if not destino.strip():
            raise ValueError("El destino es obligatorio")
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor que 0 kg")

        self._contador_id += 1
        paquete = Paquete(self._contador_id, destinatario.strip(),
                          destino.strip(), float(peso_kg), prioridad)
        self.paquetes.insertar_final(paquete)
        self.historial.apilar(("registrar", paquete))
        return paquete

    def deshacer_ultimo_registro(self) -> Paquete | None:
        """Deshace el último registro usando la pila (LIFO).

        Devuelve el paquete eliminado, o None si no hay acciones.

        Complejidad: O(1) para desapilar + O(n) para quitar el paquete
        de la lista enlazada simple (buscar y reconectar referencias).
        """
        if self.historial.esta_vacia():
            return None
        _accion, paquete = self.historial.desapilar()
        if self.paquetes.eliminar(paquete):
            if paquete.id == self._contador_id:
                self._contador_id -= 1  # reutiliza el id desecho
            return paquete
        return None

    # ------------------------------------------------------------------
    # Consultas para la vista
    # ------------------------------------------------------------------
    def listar_paquetes(self) -> list:
        """Devuelve los paquetes en orden de llegada. Recorrido O(n)."""
        return self.paquetes.a_lista()

    def total_paquetes(self) -> int:
        """Cantidad total de paquetes. O(1)."""
        return self.paquetes.tamanio()

    def total_urgentes(self) -> int:
        """Cuenta los paquetes urgentes. Recorrido O(n)."""
        return sum(1 for p in self.paquetes if p.es_urgente)

    def puede_deshacer(self) -> bool:
        """True si hay acciones en el historial. O(1)."""
        return not self.historial.esta_vacia()
