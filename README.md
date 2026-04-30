# Práctico: Map y Reduce en Python

Implementación de los paradigmas **Map** y **Reduce** usando Python puro (`functools.reduce` + `map` built-in). Todos los datasets fueron generados directamente en el código.

## Ejercicios

### 1. Map — Cuadrado de números

Dada una lista de al menos 20 números, aplicar `map` para obtener el cuadrado de cada uno y mostrar la lista resultante.

### 2. Map — Longitud de palabras

Dada una lista de al menos 30 palabras de diferente longitud, usar `map` para obtener una lista con la longitud de cada palabra.

### 3. Map — Capitalizar primera letra

Dada una lista de palabras en minúscula, usar `map` para transformar la primera letra de cada palabra a mayúscula.

### 4. Reduce — Suma de números

Usando `reduce`, sumar todos los elementos de una lista de al menos 30 números.

### 5. Reduce — Producto por escalar

Usando `reduce`, calcular el producto de todos los elementos de una lista de al menos 10 números enteros y multiplicar el resultado por un número entero dado.

### 6. Map + Reduce — Promedio de longitud de palabras

Dada una lista de palabras de diferente longitud, usar `map` para obtener las longitudes y `reduce` para calcular el promedio.

### 7. Map + Reduce — Conteo de palabras (Word Count)

Dada una lista de palabras (con repeticiones), usar `map` para transformar cada palabra en un par `{palabra: 1}` y `reduce` para acumular el conteo total de cada una.

### 8. Reduce — Promedio de notas

Dado un dataset de tuplas `(estudiante, nota)` con al menos 10 estudiantes, usar `reduce` para calcular el promedio de notas del grupo.

### 9. Reduce — Estadísticas por categoría

Dado un dataset de tuplas `(categoría, precio)`, usar `reduce` para agrupar por categoría y obtener el **promedio**, **máximo** y **mínimo** de precio por cada una.

### 10. Reduce — Accesos por IP

Dado un dataset de tuplas `(IP, recurso, tiempo)`, usar `reduce` para contar la cantidad de accesos por IP y detectar cuál es la IP más activa.

## Cómo ejecutar

```bash
python practico_mapreduce.py
```

Requiere Python 3. Sin dependencias externas.

## Nota técnica

En Python 3, `reduce` **no es un built-in** — a diferencia de `map` y `filter`. Debe importarse explícitamente:

```python
from functools import reduce
```
