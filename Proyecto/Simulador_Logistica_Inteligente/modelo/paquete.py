"""Entidad de dominio: Paquete a despachar en el centro logístico.

Avance 1 — INF-220 Estructuras de Datos I
"""


class Paquete:
    """Representa un paquete registrado en el centro de distribución."""

    PRIORIDADES = ("Normal", "Urgente")

    def __init__(self, id_paquete: int, destinatario: str, destino: str,
                 peso_kg: float, prioridad: str = "Normal"):
        if prioridad not in self.PRIORIDADES:
            raise ValueError(
                f"Prioridad inválida: {prioridad!r}. "
                f"Opciones: {self.PRIORIDADES}"
            )
        self.id = id_paquete
        self.destinatario = destinatario
        self.destino = destino
        self.peso_kg = peso_kg
        self.prioridad = prioridad
        self.estado = "Registrado"  # futuro: En tránsito, Entregado, etc.

    @property
    def es_urgente(self) -> bool:
        return self.prioridad == "Urgente"

    def __eq__(self, otro) -> bool:
        """Igualdad por identidad lógica (mismo id)."""
        if isinstance(otro, Paquete):
            return self.id == otro.id
        return NotImplemented

    def __str__(self) -> str:
        return (f"#{self.id} {self.destinatario} → {self.destino} "
                f"({self.peso_kg} kg, {self.prioridad})")

    def __repr__(self) -> str:
        return (f"Paquete(id={self.id}, destino={self.destino!r}, "
                f"prioridad={self.prioridad!r})")
