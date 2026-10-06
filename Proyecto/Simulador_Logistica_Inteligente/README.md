# Simulador de Centro Logístico de Distribución y Rutas de Despacho

**INF-220 · Estructuras de Datos I — Avance 1 (primera parte)**

Proyecto realizado en Python usando la librería **Flet** para la interfaz gráfica,
siguiendo el patrón **Modelo-Vista-Controlador (MVC)**. Todas las estructuras de
datos están implementadas desde cero, utilizando nodos y referencias, sin apoyarse
en las colecciones nativas de Python.

Este es el **primer avance** del proyecto. Aquí solo se desarrolló el registro de
paquetes y el deshacer de acciones. Las colas, las rutas de despacho y la
persistencia de datos quedarán para los siguientes avances.

## Cómo ejecutar

Requisitos: Python 3.10 o superior.

```bash
pip install flet      # solo la primera vez
python main.py        # abre la ventana en el escritorio
```

## Estructura del proyecto

```
Simulador_Logistica_Inteligente/
├── main.py                     # Punto de entrada: conecta Modelo, Vista y Controlador
├── README.md
├── estructuras/                # Estructuras de datos implementadas desde cero
│   ├── nodo.py                 # Nodo y NodoDoble
│   ├── lista_enlazada.py       # Lista enlazada simple (completa)
│   ├── lista_doble.py          # Lista doble (parcial)
│   └── pila.py                 # Pila LIFO
├── modelo/                     # Modelo del MVC
│   ├── paquete.py              # Entidad Paquete
│   └── centro_logistico.py     # Inventario (lista) y historial (pila)
├── controlador/
│   └── controlador.py          # Validación y orquestación
├── vista/
│   └── app_vista.py            # Interfaz gráfica en Flet
└── datos/                      # Pendiente: guardado en JSON
```

## Qué se implementó en este avance

| Componente | Estado | Detalle |
|---|---|---|
| Patrón MVC | Completo | Modelo, Vista y Controlador desacoplados |
| Nodo y NodoDoble | Completo | Nodos con referencias siguiente / anterior |
| Lista enlazada simple | Completo | Insertar, buscar, eliminar, recorrer, tamaño |
| Pila LIFO | Completo | Apilar, desapilar, cima, recorrido |
| Lista doble | Parcial | Solo inserción y recorrido bidireccional |
| Interfaz Flet | Parcial | Formulario, lista de paquetes y estadísticas |
| Deshacer registro | Completo | Funciona mediante la pila (LIFO) |
| Entidad Paquete | Completo | Con prioridad Normal y Urgente |

## Qué falta para los siguientes avances

- Cola FIFO para los despachos en orden de llegada.
- Cola de prioridad para que los paquetes urgentes salgan primero.
- Cola circular para el buffer de vehículos y rutas.
- Completar la lista doble (eliminar y buscar) y crear la lista circular.
- Rehacer, usando doble pila (hasta ahora solo está Deshacer).
- Rutas de despacho y asignación de paquetes a vehículos.
- Guardado de datos en archivos JSON dentro de la carpeta `datos/`.
- Pruebas unitarias y análisis de complejidad O(1) contra O(n).

## Complejidad de las operaciones

| Estructura | Operación | Complejidad |
|---|---|---|
| Lista simple | insertar_inicio | O(1) |
| Lista simple | insertar_final, buscar, eliminar | O(n) |
| Lista doble | insertar_inicio / insertar_final | O(1) |
| Pila | apilar, desapilar, cima | O(1) |
| Modelo | registrar_paquete | O(1) |
| Modelo | deshacer_ultimo_registro | O(1) + O(n) |
| Modelo | total_urgentes | O(n) |

## Validación rápida por consola

```bash
python - <<'PY'
from modelo.centro_logistico import CentroLogistico

c = CentroLogistico()
c.registrar_paquete("Ana", "La Paz", 10, "Urgente")
c.registrar_paquete("Luis", "Cochabamba", 2.5)
print(c.listar_paquetes(), "| urgentes:", c.total_urgentes())
print("Deshacer ->", c.deshacer_ultimo_registro())
print("Ahora hay:", c.total_paquetes(), "paquete(s)")
PY
```
