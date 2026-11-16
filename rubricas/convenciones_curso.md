# Convenciones de Código del Curso (Basado en Camilo Rocha)

Todo código en Python implementado en este repositorio debe seguir rigurosamente estas convenciones:

- **Idioma:** Los identificadores de variables, funciones y los comentarios se escriben en **inglés**.
- **Arreglos:** Las listas de Python actúan como arreglos con índices basados desde `0`.
- **Infinito:** La constante `INF` se define explícitamente como `float("inf")` para representar $+ \infty$ en rangos vacíos o costos máximos.
- **Puntos de salida en ciclos:** Los ciclos deben tener un único punto de salida o utilizar centinelas en su condición, **evitando retornos tempranos (`return`) desde el interior del ciclo**.
- **Nombres de funciones:** El nombre de una función debe describir **qué calcula**, no cómo lo calcula.
- **Precondiciones:** Cada función supone su precondición y no la verifica internamente. Se debe documentar explícitamente mediante un comentario que comience con `pre:` al inicio de la función.
- **Valores de retorno según el tipo de problema (Tabla 4):**
  - *Decisión:* Retorna un `bool`.
  - *Búsqueda:* Retorna el testigo o `None` si no existe.
  - *Optimización (testigo):* Retorna el testigo óptimo o `None`.
  - *Optimización (valor):* Retorna un número o `INF` si no hay testigos.
  - *Conteo:* Retorna un `int` (`0` si no hay testigos).
  - *Enumeración:* Retorna una `list` (vacía si no hay testigos).