"""Controlador del patron MVC: enlaza la Vista con el Modelo.

Recibe las acciones de la interfaz, las convierte en operaciones
sobre la ListaSimple y vuelve a dibujar el resultado en la vista.
"""


class ControladorLista:
    """Une la ListaSimple (modelo) con la VistaPrincipal (vista)."""

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self._nodo_apartado = None
        self.vista.asignar_controlador(self)
        self._refrescar_vista()

    def insertar_al_inicio(self, valor):
        """Agrega un valor al principio de la lista."""
        if not self._validar_valor(valor):
            return
        self.modelo.insertar_al_inicio(valor)
        self.vista.limpiar_entrada()
        self.vista.mostrar_mensaje_info(f"Dato '{valor}' agregado al principio.")
        self._refrescar_vista()

    def insertar_al_final(self, valor):
        """Agrega un valor al final de la lista."""
        if not self._validar_valor(valor):
            return
        self.modelo.insertar_al_final(valor)
        self.vista.limpiar_entrada()
        self.vista.mostrar_mensaje_info(f"Dato '{valor}' agregado al final.")
        self._refrescar_vista()

    def buscar(self, valor):
        """Comprueba si el valor existe y avisa al usuario."""
        if not self._validar_valor(valor):
            return

        nodo = self.modelo.buscar(valor)
        if nodo is None:
            self.vista.mostrar_dialogo_error(
                "Consulta", f"El dato '{valor}' no aparece en la lista.")
            self.vista.mostrar_mensaje_error(
                f"El dato '{valor}' no aparece en la lista.")
        else:
            self.vista.mostrar_dialogo_info(
                "Consulta", f"El dato '{valor}' si esta en la lista.")
            self.vista.mostrar_mensaje_info(f"Dato '{valor}' localizado.")

    def eliminar(self, valor):
        """Desconecta el valor de la lista y lo deja apartado.

        El nodo deja de formar parte de la cadena, pero por ahora
        sigue ocupando espacio en memoria.
        """
        if not self._validar_valor(valor):
            return

        nodo = self.modelo.eliminar_por_valor(valor)
        self.vista.limpiar_entrada()
        if nodo is None:
            self.vista.mostrar_mensaje_error(
                f"El dato '{valor}' no estaba en la lista.")
            return

        self._nodo_apartado = nodo
        self.vista.mostrar_mensaje_info(
            f"Dato '{valor}' quitado de la lista.")
        self._refrescar_vista()

    def eliminar_fisicamente(self):
        """Libera la memoria del bloque que estaba apartado (si lo hay)."""
        if self._nodo_apartado is None:
            self.vista.mostrar_mensaje_error(
                "No tienes ningun bloque apartado. "
                "Pulsa primero 'Quitar'.")
            return

        valor = self._nodo_apartado.valor
        self.modelo.liberar_nodo(self._nodo_apartado)
        self._nodo_apartado = None
        self.vista.mostrar_mensaje_info(
            "Memoria liberada")
        self._refrescar_vista()

    def _validar_valor(self, valor):
        if not valor or not valor.strip():
            self.vista.mostrar_mensaje_error("Ingresa un dato para continuar")
            return False
        return True

    def _refrescar_vista(self):
        if self.modelo.esta_vacia():
            self.vista.mostrar_mensaje_info("La lista esta vacia")
        # Redibuja los bloques
        self.vista.actualizar_lista(
            list(self.modelo.recorrer()),
            self._nodo_apartado.valor if self._nodo_apartado else None)
