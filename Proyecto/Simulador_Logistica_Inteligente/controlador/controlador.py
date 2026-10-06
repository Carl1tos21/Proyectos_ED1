"""Controlador (C) del patrón MVC.

Avance 1 — INF-220 Estructuras de Datos I

Recibe los eventos de la vista, valida las entradas, invoca al Modelo
y le pide a la Vista que se actualice. NO contiene lógica de interfaz
ni estructura de datos: solo orquestación.
"""


class Controlador:
    """Conecta la Vista (Flet) con el Modelo (CentroLogistico)."""

    def __init__(self):
        from modelo.centro_logistico import CentroLogistico
        self.modelo = CentroLogistico()
        self.vista = None  # se inyecta desde main.py (DI)

    # ------------------------------------------------------------------
    # Eventos de la vista
    # ------------------------------------------------------------------
    def registrar_paquete(self, destinatario: str, destino: str,
                          peso_txt: str, prioridad: str) -> bool:
        """Valida la entrada y registra el paquete en el modelo.

        Devuelve True si el registro fue exitoso; False si hay error
        (el motivo se notifica a través de la vista).
        """
        # --- Validación de entradas (responsabilidad del controlador) ---
        if not destinatario.strip() or not destino.strip():
            self.vista.notificar(
                "Destinatario y destino son obligatorios", error=True)
            return False
        try:
            peso = float(peso_txt.strip().replace(",", "."))
        except ValueError:
            self.vista.notificar(
                f"Peso inválido: {peso_txt!r} no es un número", error=True)
            return False
        if peso <= 0:
            self.vista.notificar("El peso debe ser mayor que 0 kg", error=True)
            return False

        # --- Llamada al modelo ---
        try:
            paquete = self.modelo.registrar_paquete(
                destinatario, destino, peso, prioridad
            )
        except ValueError as exc:
            self.vista.notificar(str(exc), error=True)
            return False

        self.refrescar()
        self.vista.notificar(f"Paquete {paquete} registrado ✔")
        return True

    def deshacer_registro(self) -> None:
        """Deshace el último registro usando la pila del historial."""
        if not self.modelo.puede_deshacer():
            self.vista.notificar(
                "Nada que deshacer: el historial está vacío", error=True)
            return
        paquete = self.modelo.deshacer_ultimo_registro()
        if paquete is not None:
            self.refrescar()
            self.vista.notificar(f"Se deshizo el registro de {paquete}")

    def refrescar(self) -> None:
        """Solicita a la vista que repinte los datos actuales del modelo."""
        if self.vista is not None:
            self.vista.actualizar(
                paquetes=self.modelo.listar_paquetes(),
                total=self.modelo.total_paquetes(),
                urgentes=self.modelo.total_urgentes(),
                siguiente_id=self.modelo.siguiente_id(),
                puede_deshacer=self.modelo.puede_deshacer(),
            )
