"""Vista (V) del patrón MVC — interfaz construida con Flet.

Avance 1 — INF-220 Estructuras de Datos I

La vista SOLO dibuja y reporta eventos al controlador; no toca las
estructuras de datos ni contiene reglas de negocio.

Funcionalidad del avance 1:
  - Registrar paquete (formulario con validación visual).
  - Lista de paquetes registrados (lista enlazada del modelo).
  - Botón "Deshacer último registro" (pila LIFO del historial).
  - Estadísticas básicas.

PENDIENTE: pestañas de colas, prioridades, rutas y persistencia.
"""

import flet as ft


class VistaSimulador:
    """Interfaz gráfica del Simulador de Centro Logístico."""

    def __init__(self, page: ft.Page, controlador):
        self.page = page
        self.ctrl = controlador

    # ------------------------------------------------------------------
    # Construcción de la interfaz
    # ------------------------------------------------------------------
    def construir(self) -> None:
        page = self.page
        page.title = "Simulador de Centro Logístico — INF-220 (Avance 1)"
        page.bgcolor = ft.Colors.SURFACE
        page.padding = 20
        page.vertical_alignment = ft.CrossAxisAlignment.START
        if hasattr(page, "window"):
            page.window.width = 1100
            page.window.height = 720

        # --- Formulario de registro ---
        self.txt_destinatario = ft.TextField(
            label="Destinatario", hint_text="Ej. Ana García", expand=True)
        self.txt_destino = ft.TextField(
            label="Destino", hint_text="Ej. La Paz - Zona Sur", expand=True)
        self.txt_peso = ft.TextField(
            label="Peso (kg)", hint_text="Ej. 12.5", width=140)
        self.ddl_prioridad = ft.Dropdown(
            label="Prioridad", width=160, value="Normal",
            options=[ft.DropdownOption(key=p, text=p)
                     for p in ("Normal", "Urgente")])

        self.btn_registrar = ft.FilledButton(
            "Registrar paquete", icon=ft.Icons.ADD_SHOPPING_CART,
            on_click=self._al_registrar)
        self.btn_deshacer = ft.OutlinedButton(
            "Deshacer último", icon=ft.Icons.UNDO, disabled=True,
            on_click=self._al_deshacer)

        formulario = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Registrar paquete", size=18,
                            weight=ft.FontWeight.BOLD),
                    ft.Row([self.txt_destinatario, self.txt_destino]),
                    ft.Row([self.txt_peso, self.ddl_prioridad], spacing=12),
                    ft.Row([self.btn_registrar, self.btn_deshacer],
                           spacing=12),
                ], spacing=12),
                padding=16,
            ),
            margin=ft.Margin.only(bottom=16),
        )

        # --- Estadísticas ---
        self.lbl_total = ft.Text("Paquetes: 0", size=16,
                                 weight=ft.FontWeight.BOLD)
        self.lbl_urgentes = ft.Text("Urgentes: 0", size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.RED)
        self.lbl_siguiente = ft.Text("Próximo ID: #1", size=16,
                                     weight=ft.FontWeight.BOLD,
                                     color=ft.Colors.BLUE)
        estadisticas = ft.Row(
            [self.lbl_total, self.lbl_urgentes, self.lbl_siguiente],
            spacing=24)

        # --- Lista de paquetes ---
        self.lista_vista = ft.ListView(expand=True, spacing=8)

        panel_paquetes = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text("Paquetes registrados (lista enlazada simple)",
                            size=16, weight=ft.FontWeight.BOLD),
                    estadisticas,
                    self.lista_vista,
                ], spacing=12, expand=True),
                padding=16,
                height=380,
            ),
        )

        pie = ft.Text(
            "Avance 1 — MVC + Flet + Lista simple, Lista doble (parcial) y "
            "Pila LIFO. Pendientes: colas (FIFO/prioridad/circular), lista "
            "circular, Undo/Redo completo y persistencia.",
            size=12, opacity=0.7, text_align=ft.TextAlign.CENTER)

        page.add(formulario, panel_paquetes, pie)
        self.ctrl.refrescar()

    # ------------------------------------------------------------------
    # Eventos -> controlador
    # ------------------------------------------------------------------
    def _al_registrar(self, _event=None) -> None:
        """Envía el formulario al controlador y limpia los campos."""
        ok = self.ctrl.registrar_paquete(
            self.txt_destinatario.value or "",
            self.txt_destino.value or "",
            self.txt_peso.value or "",
            self.ddl_prioridad.value or "Normal",
        )
        if ok:
            self.txt_destinatario.value = ""
            self.txt_destino.value = ""
            self.txt_peso.value = ""
            self.page.update()

    def _al_deshacer(self, _event=None) -> None:
        """Pide al controlador deshacer el último registro (pila LIFO)."""
        self.ctrl.deshacer_registro()

    # ------------------------------------------------------------------
    # Actualización (llamada por el controlador)
    # ------------------------------------------------------------------
    def actualizar(self, paquetes: list, total: int, urgentes: int,
                   siguiente_id: int, puede_deshacer: bool) -> None:
        """Repinta estadísticas y lista de paquetes."""
        self.lbl_total.value = f"Paquetes: {total}"
        self.lbl_urgentes.value = f"Urgentes: {urgentes}"
        self.lbl_siguiente.value = f"Próximo ID: #{siguiente_id}"
        self.btn_deshacer.disabled = not puede_deshacer

        self.lista_vista.controls.clear()
        if not paquetes:
            self.lista_vista.controls.append(
                ft.Text("Sin paquetes registrados todavía.",
                        italic=True, opacity=0.6))
        else:
            fondo = (ft.Colors.SURFACE_CONTAINER_HIGHEST
                     if hasattr(ft.Colors, "SURFACE_CONTAINER_HIGHEST")
                     else ft.Colors.WHITE)
            for p in reversed(paquetes):  # los más recientes arriba
                color = (ft.Colors.RED_500 if p.es_urgente
                         else ft.Colors.BLUE_700)
                self.lista_vista.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Text(f"#{p.id}", weight=ft.FontWeight.BOLD,
                                    color=color),
                            ft.Text(p.destinatario, expand=True),
                            ft.Text(p.destino, expand=True),
                            ft.Text(f"{p.peso_kg:g} kg"),
                            ft.Container(
                                content=ft.Text(p.prioridad, size=12,
                                                color=ft.Colors.WHITE),
                                bgcolor=color,
                                padding=ft.Padding.symmetric(
                                    vertical=4, horizontal=10),
                                border_radius=12,
                            ),
                        ], spacing=12),
                        bgcolor=fondo,
                        padding=12,
                        border_radius=8,
                    ))
        self.page.update()

    def notificar(self, mensaje: str, error: bool = False) -> None:
        """Muestra un SnackBar con el mensaje enviado por el controlador."""
        snack = ft.SnackBar(
            ft.Text(mensaje),
            bgcolor=ft.Colors.ERROR if error else ft.Colors.GREEN,
        )
        # Flet 1.0 usa show_dialog; versiones antiguas usaban page.open
        if hasattr(self.page, "show_dialog"):
            self.page.show_dialog(snack)
        else:
            self.page.open(snack)
        self.page.update()
