"""Punto de arranque de la aplicacion (patron MVC).

Uso:
    python main.py
"""

from modelo.lista_simple import ListaSimple
from vista.vista_principal import VistaPrincipal
from controlador.controlador_lista import ControladorLista


def main():
    modelo = ListaSimple()
    vista = VistaPrincipal()
    ControladorLista(modelo, vista)
    vista.mainloop()


if __name__ == "__main__":
    main()
