"""
Interfaz grafica con Tkinter para manejar la ListaSimple.

"""

import tkinter as tk
from tkinter import ttk, messagebox


class VistaPrincipal(tk.Tk):
    """Ventana principal para interactuar con la ListaSimple."""

    def __init__(self):
        super().__init__()
        self.title("Practica de Lista Enlazada")
        self.geometry("540x540")
        self.resizable(False, False)

        self._controlador = None
        self._construir_widgets()

    def asignar_controlador(self, controlador):
        """Conecta esta vista con su controlador."""
        self._controlador = controlador

    def _construir_widgets(self):
        contenedor = ttk.Frame(self, padding=15)
        contenedor.pack(fill="both", expand=True)

        # --- Campo de dato ---
        marco_entrada = ttk.Frame(contenedor)
        marco_entrada.pack(fill="x", pady=(0, 10))

        ttk.Label(marco_entrada, text="Dato:").pack(side="left")
        self.entrada_valor = ttk.Entry(marco_entrada)
        self.entrada_valor.pack(side="left", fill="x", expand=True, padx=5)
        self.entrada_valor.bind(
            "<Return>", lambda evento: self._on_insertar_final())

        # --- Botones de accion ---
        marco_botones = ttk.Frame(contenedor)
        marco_botones.pack(fill="x", pady=(0, 10))

        ttk.Button(
            marco_botones, text="Agregar al inicio",
            command=self._on_insertar_inicio
        ).pack(side="left", expand=True, fill="x", padx=2)

        ttk.Button(
            marco_botones, text="Agregar al final",
            command=self._on_insertar_final
        ).pack(side="left", expand=True, fill="x", padx=2)

        marco_botones2 = ttk.Frame(contenedor)
        marco_botones2.pack(fill="x", pady=(0, 10))

        ttk.Button(
            marco_botones2, text="Consultar",
            command=self._on_buscar
        ).pack(side="left", expand=True, fill="x", padx=2)

        ttk.Button(
            marco_botones2, text="Quitar",
            command=self._on_eliminar
        ).pack(side="left", expand=True, fill="x", padx=2)

        marco_botones3 = ttk.Frame(contenedor)
        marco_botones3.pack(fill="x", pady=(0, 10))

        ttk.Button(
            marco_botones3, text="Borrar de memoria",
            command=self._on_eliminar_fisicamente
        ).pack(side="left", expand=True, fill="x", padx=2)

        # --- Zona de dibujo de la lista ---
        marco_lista = ttk.LabelFrame(
            contenedor, text="Elementos de la lista", padding=10)
        marco_lista.pack(fill="both", expand=True, pady=(0, 10))

        # Lienzo donde se dibujan los vagones conectados en horizontal.
        self.lienzo = tk.Canvas(marco_lista, height=200, bg="white")
        self.lienzo.pack(fill="both", expand=True)

        self._PALETA = [
            "#c0392b",  # rojo oscuro
            "#d35400",  # naranja quemado
            "#f39c12",  # ambar
            "#27ae60",  # verde
            "#2980b9",  # azul
            "#8e44ad",  # morado
            "#16a085",  # verde azulado
            "#d81b60",  # rosa fuerte
        ]

        # --- Mensajes de estado ---
        self.etiqueta_estado = ttk.Label(
            contenedor, foreground="#2c7a7b")
        self.etiqueta_estado.pack(fill="x")

    # --- Manejadores de eventos: delegan al controlador ---

    def _on_insertar_inicio(self):
        if self._controlador:
            self._controlador.insertar_al_inicio(self.entrada_valor.get())

    def _on_insertar_final(self):
        if self._controlador:
            self._controlador.insertar_al_final(self.entrada_valor.get())

    def _on_buscar(self):
        if self._controlador:
            self._controlador.buscar(self.entrada_valor.get())

    def _on_eliminar(self):
        if self._controlador:
            self._controlador.eliminar(self.entrada_valor.get())

    def _on_eliminar_fisicamente(self):
        if self._controlador:
            self._controlador.eliminar_fisicamente()

    # --- Metodos que el controlador usa para actualizar la vista ---

    def limpiar_entrada(self):
        self.entrada_valor.delete(0, tk.END)

    def mostrar_mensaje_info(self, mensaje):
        self.etiqueta_estado.config(text=mensaje, foreground="#2c7a7b")

    def mostrar_mensaje_error(self, mensaje):
        self.etiqueta_estado.config(text=mensaje, foreground="#b03a2e")

    def mostrar_dialogo_info(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_dialogo_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    def actualizar_lista(self, valores, nodo_apartado=None):
        """
        Cada nodo se muestra como un bloque,
        conectados por flechas. La lista refleja SIEMPRE su estado real:
        al eliminar un nodo, los bloques se acomodan y el eliminado se
        dibuja aparte

        Args:
            valores: iterable con los valores en orden (cabeza a cola).
            nodo_apartado: valor del nodo desenlazado que aun existe en
                memoria, o None si no hay ninguno.
        """
        self.lienzo.delete("all")

        d = 46  # tamano del bloque (lado)
        x = 20
        y = 25

        n = len(valores)
        if n == 0 and nodo_apartado is None:
            self.lienzo.create_text(
                270, 30, anchor="n",
                text="La lista aun no tiene elementos",
                font=("Segoe UI", 11, "italic"), fill="#999999")
            return

        # Tren principal (nodos reales de la lista).
        for i, valor in enumerate(valores):
            color = self._PALETA[i % len(self._PALETA)]
            self._dibujar_bloque(x, y, d, str(valor), color, "black")
            if i < len(valores) - 1:
                # Flecha hacia el siguiente nodo (conexion por el centro).
                self.lienzo.create_line(x + d, y + d // 2,
                                        x + d + 22, y + d // 2,
                                        arrow=tk.LAST, width=2,
                                        fill="black")
            x += d + 22

        # Nodo desenlazado que aun existe en memoria: se dibuja aparte,
        # debajo, en gris, sin conexiones.
        if nodo_apartado is not None:
            ay = y + d + 50  # debajo de la fila del tren
            # Rotulo que explica que aun esta en memoria.
            self.lienzo.create_text(
                20, ay, anchor="w",
                text="Dato fuera de la lista (todavia ocupa memoria):",
                font=("Segoe UI", 9, "italic"), fill="#555555")
            # Bloque gris con el valor, sin flecha de conexion.
            self._dibujar_bloque(20, ay + 18, d, str(nodo_apartado),
                                 "#95a5a6", "#7f8c8d")
            # Leyenda breve sobre como liberarlo.
            self.lienzo.create_text(
                20 + d + 12, ay + 18 + d // 2, anchor="w",
                text="pulsa 'Borrar de memoria'\npara dejar de usarlo",
                font=("Segoe UI", 8), fill="#7f8c8d")


    def _dibujar_bloque(self, x, y, d, texto, relleno, borde):
        """Dibuja un bloque con su valor dentro.

        Args:
            x, y: esquina superior izquierda del bloque.
            d: tamano del lado del bloque (cuadrado).
            texto: valor a mostrar dentro del bloque.
            relleno: color de fondo del bloque.
            borde: color del borde del bloque.
        """
        self.lienzo.create_rectangle(
            x, y, x + d, y + d,
            fill=relleno, outline=borde, width=2)
        self.lienzo.create_text(
            x + d // 2, y + d // 2, text=texto,
            font=("Segoe UI", 12, "bold"), fill="white")
