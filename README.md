# Proyectos_ED1

Repositorio con los avances y proyectos de la materia de **Estructuras de
Datos 1** del Ing. Juan Carlos Peinado Pereira.

Aquí se suben las tareas y sus avances, más el proyecto final de la materia.

---

## Contenido

| Carpeta | Descripción | Estado |
|---|---|---|
| `Tareas/Listas_Enlazadas` | Lista enlazada simple en Python con ventana gráfica (patrón MVC) | Completo |
| `Proyecto/Simulador_Logistica_Inteligente` | Simulador de centro logístico con Flet (MVC y estructuras desde cero) | Avance 1 |

## Estructura del repositorio

```
Proyectos_ED1/
├── README.md
├── .gitignore
├── Tareas/
│   └── Listas_Enlazadas/
│       ├── README.md              # Explicación completa
│       ├── main.py                # Punto de entrada (ventana gráfica)
│       ├── 01_lista_simple.py      # Versión corta por terminal
│       ├── modelo/
│       │   └── lista_simple.py     # La lista enlazada
│       ├── vista/
│       │   └── vista_principal.py  # Ventana con Tkinter
│       └── controlador/
│           └── controlador_lista.py
└── Proyecto/
    └── Simulador_Logistica_Inteligente/
        ├── README.md              # Explicación del avance
        ├── main.py                # Punto de entrada (ventana Flet)
        ├── estructuras/           # Lista simple, lista doble y pila
        ├── modelo/                # Paquete y centro logístico
        ├── controlador/
        ├── vista/
        └── datos/                 # Pendiente: guardado en JSON
```

## Listas Enlazadas

Práctica de listas enlazadas con interfaz gráfica. Se pueden agregar nodos
al inicio y al final, consultar si un valor existe, quitar un nodo de la
lista y liberarlo de la memoria.

Cada carpeta tiene su propio `README.md` con la explicación detallada.
Resumen:

```bash
cd Tareas/Listas_Enlazadas
python3 main.py          # abre la ventana gráfica
python3 01_lista_simple.py   # versión por terminal
```

Requisitos: Python 3 y Tkinter (incluido por defecto en la mayoría de
sistemas).

## Proyecto: Simulador Logístico Inteligente

Simulador de centro logístico de distribución y rutas de despacho
(**INF-220 · Avance 1**). Está hecho con el patrón MVC y la librería Flet
para la interfaz. Todas las estructuras de datos (lista enlazada, lista
doble y pila) están implementadas desde cero, con nodos y referencias.

En este primer avance se desarrolló el registro de paquetes y el deshacer
de acciones mediante la pila. Las colas, las rutas de despacho y el guardado
en archivos quedan para los siguientes avances.

Para ejecutarlo:

```bash
cd Proyecto/Simulador_Logistica_Inteligente
pip install flet         # solo la primera vez
python3 main.py          # abre la ventana en el escritorio
```

Requisitos: Python 3.10 o superior. La explicación completa está en el
`README.md` de la carpeta del proyecto.

## Cómo se organizan los avances

Cada avance o corrección se sube como un commit con un mensaje que explica
qué cambió, para que se pueda ver la evolución del trabajo.

