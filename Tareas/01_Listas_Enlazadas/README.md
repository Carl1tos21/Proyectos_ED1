# Lista Enlazada Simple

Práctica de la materia de estructuras de datos. El proyecto implementa una
lista enlazada simple en Python y tiene una ventana gráfica para ver y
manipular la lista.

---

## ¿Qué es una lista enlazada?

Es una estructura de datos donde los elementos se guardan en nodos. Cada nodo
tiene dos cosas:

- el dato que guarda
- una referencia (puntero) al siguiente nodo

Los nodos no están uno al lado del otro en memoria, sino que se conectan
entre sí. El primer nodo se llama cabeza y el último apunta a `None`.

```
[10] -> [20] -> [30] -> None
```

A diferencia de una lista de Python común, para llegar a un elemento hay que
recorrer los nodos desde la cabeza, uno por uno.

## Estructura del proyecto

El proyecto está organizado con el patrón MVC (Modelo - Vista - Controlador):

```
Listas_Enlazadas/
├── main.py                      # Punto de entrada
├── 01_lista_simple.py           # Versión corta de la lista (ejercicio)
├── .gitignore
├── modelo/
│   ├── __init__.py
│   └── lista_simple.py          # La lista enlazada
├── vista/
│   ├── __init__.py
│   └── vista_principal.py       # Ventana con Tkinter
└── controlador/
    ├── __init__.py
    └── controlador_lista.py     # Conecta la vista con el modelo
```

### Modelo (modelo/lista_simple.py)

Es el centro del proyecto. Tiene la clase `Nodo` y la clase `ListaSimple`.

Clase Nodo:

- `valor`: el dato que guarda
- `siguiente`: referencia al siguiente nodo (o `None` si es el último)

Clase ListaSimple:

- `insertar_al_inicio(valor)`: agrega un nodo al principio de la lista.
- `insertar_al_final(valor)`: agrega un nodo al final. Guarda también un
  puntero a la cola para no tener que recorrer toda la lista cada vez.
- `buscar(valor)`: devuelve el nodo si existe, o `None` si no está.
- `eliminar_por_valor(valor)`: desconecta el primer nodo que tenga ese valor.
- `liberar_nodo(nodo)`: libera físicamente el nodo de la memoria usando
  `gc.collect()`.
- `recorrer()`: devuelve los valores de la lista en orden.

Además se puede recorrer con `for valor in lista` y mostrar con `print(lista)`.

### Vista (vista/vista_principal.py)

Es la ventana gráfica hecha con Tkinter. Tiene:

- un campo para escribir el dato
- botones: Agregar al inicio, Agregar al final, Consultar, Quitar y
  Borrar de memoria
- un canvas donde se dibuja la lista como bloques conectados con flechas
- una etiqueta abajo con mensajes de estado

Cuando se quita un nodo de la lista, la ventana lo dibuja abajo en color
gris, aparte de los demás, para mostrar que ya no pertenece a la lista pero
todavía ocupa memoria.

### Controlador (controlador/controlador_lista.py)

Es el intermediario entre los otros dos. Recibe los clics de la ventana,
valida que se haya escrito un dato, llama al modelo y luego vuelve a dibujar
la vista con el resultado. También muestra las alertas cuando se consulta un
dato que no existe.

### main.py

Crea el modelo, la vista y el controlador, los conecta y abre la ventana.

### 01_lista_simple.py

Es la versión corta de la lista enlazada, sin ventana gráfica. Sirve para
probar la estructura desde la terminal. Si se ejecuta muestra:

```
10 -> 20 -> 30 -> None
¿Esta el 20?: True
Quitar 20: True
10 -> 30 -> None
```

## Quitar un nodo vs borrarlo de memoria

Este es el detalle más importante de la práctica:

1. **Quitar (eliminación lógica)**: el nodo se desconecta de la cadena y ya
   no forma parte de la lista, pero todavía existe en memoria. En la ventana
   se ve como un bloque gris aparte.
2. **Borrar de memoria (eliminación física)**: se libera el espacio que
   ocupaba el nodo. En la consola aparece un mensaje como este:

```
[MEM] Nodo(20) dejo de usarse y se libera.
```

## Requisitos

- Python 3
- Tkinter (viene incluido con Python en la mayoría de sistemas)

En Ubuntu o Debian, si Tkinter no está instalado:

```bash
sudo apt install python3-tk
```

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python3 main.py
```

Para probar la versión corta por terminal:

```bash
python3 01_lista_simple.py
```

## Ejemplo de uso

1. Escribir un dato en el campo y presionar "Agregar al final" (o
   "Agregar al inicio").
2. Presionar "Consultar" para ver si el dato está en la lista. Sale una
   ventana con el resultado, ya sea que exista o no.
3. Presionar "Quitar" para desconectar el nodo de la lista.
4. Presionar "Borrar de memoria" para liberar el espacio del nodo que
   estaba apartado.

## Autor

Carlos Daniel
