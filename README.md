# Proyectos_ED1

Repositorio con los avances y proyectos de la materia de **Estructuras de
Datos 1** del Ing. Juan Carlos Peinado Pereira.

Aquí se suben las tareas y sus avances, más el proyecto final de la materia.

---

## Contenido

| Carpeta | Descripción | Estado |
|---|---|---|
| `Tareas/01_Listas_Enlazadas` | Lista enlazada simple en Python con ventana gráfica (patrón MVC) | Completo |
| `Proyecto/` | Proyecto final de la materia | Pendiente |

## Estructura del repositorio

```
Proyectos_ED1/
├── README.md
├── .gitignore
├── Tareas/
│   └── 01_Listas_Enlazadas/
│       ├── README.md              # Explicación completa de la tarea
│       ├── main.py                # Punto de entrada (ventana gráfica)
│       ├── 01_lista_simple.py      # Versión corta por terminal
│       ├── modelo/
│       │   └── lista_simple.py     # La lista enlazada
│       ├── vista/
│       │   └── vista_principal.py  # Ventana con Tkinter
│       └── controlador/
│           └── controlador_lista.py
└── Proyecto/
    └── (proyecto final, pendiente)
```

## Tarea 01: Lista Enlazada Simple

Práctica de listas enlazadas con interfaz gráfica. Se pueden agregar nodos
al inicio y al final, consultar si un valor existe, quitar un nodo de la
lista y liberarlo de la memoria.

Cada tarea tiene su propio `README.md` con la explicación detallada.
Resumen de la tarea 01:

```bash
cd Tareas/01_Listas_Enlazadas
python3 main.py          # abre la ventana gráfica
python3 01_lista_simple.py   # versión por terminal
```

Requisitos: Python 3 y Tkinter (incluido por defecto en la mayoría de
sistemas).

## Cómo se organizan los avances

Cada avance o corrección se sube como un commit con un mensaje que explica
qué cambió, para que se pueda ver la evolución del trabajo.

## Autor

Carlos Daniel
