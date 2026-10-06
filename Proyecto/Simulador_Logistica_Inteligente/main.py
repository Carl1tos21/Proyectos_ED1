"""Simulador de Centro Logístico de Distribución y Rutas de Despacho.

INF-220 Estructuras de Datos I — Avance 1
Patrón de diseño: Modelo-Vista-Controlador (MVC)

Punto de entrada principal: aquí se conectan (wiring) las tres capas.
"""

import flet as ft

from controlador.controlador import Controlador
from vista.app_vista import VistaSimulador


def main(page: ft.Page) -> None:
    """Configura la página y conecta Modelo <-> Controlador <-> Vista."""
    controlador = Controlador()                 # C: orquesta modelo y vista
    vista = VistaSimulador(page, controlador)   # V: interfaz Flet
    controlador.vista = vista                   # inyección de la vista al C
    vista.construir()                           # pinta el estado inicial


if __name__ == "__main__":
    ft.run(main)
