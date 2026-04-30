import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from functools import reduce

# ==============================================================================
# PRÁCTICO: MAP y REDUCE en Python
# ==============================================================================


def separador(titulo):
    print(f"\n{'=' * 60}")
    print(f"  {titulo}")
    print('=' * 60)


# ==============================================================================
# 1. Map → cuadrados de al menos 20 números
# ==============================================================================
separador("1. MAP — Cuadrados de una lista de números")

numeros_1 = [3, 7, 12, 5, 19, 2, 45, 8, 23, 11,
             34, 6, 17, 99, 4, 28, 50, 13, 41, 66]

cuadrados = list(map(lambda x: x ** 2, numeros_1))

print(f"Original : {numeros_1}")
print(f"Cuadrados: {cuadrados}")


# ==============================================================================
# 2. Map → longitudes de al menos 30 palabras
# ==============================================================================
separador("2. MAP — Longitud de cada palabra")

palabras_2 = [
    "sol", "mariposa", "computadora", "río", "elefante",
    "luz", "programación", "montaña", "pez", "universidad",
    "árbol", "inteligencia", "mar", "tecnología", "piedra",
    "nube", "conocimiento", "flor", "desarrollo", "libro",
    "dato", "algoritmo", "puerta", "ingeniero", "red",
    "sistema", "base", "estructura", "lenguaje", "variable",
]

longitudes = list(map(len, palabras_2))

for palabra, longitud in zip(palabras_2, longitudes):
    print(f"  {palabra:<20} → {longitud}")


# ==============================================================================
# 3. Map → primera letra en mayúscula
# ==============================================================================
separador("3. MAP — Capitalizar primera letra")

palabras_3 = [
    "hola", "mundo", "python", "reduce", "función",
    "lista", "dato", "nodo", "grafo", "árbol",
]

capitalizadas = list(map(lambda p: p[0].upper() + p[1:], palabras_3))

print(f"Original   : {palabras_3}")
print(f"Capitalizado: {capitalizadas}")


# ==============================================================================
# 4. Reduce → suma de al menos 30 números
# ==============================================================================
separador("4. REDUCE — Suma de una lista de números")

numeros_4 = [
    14, 7, 33, 21, 9, 45, 62, 18, 5, 37,
    11, 28, 50, 3, 44, 16, 72, 29, 8, 55,
    41, 6, 19, 88, 13, 34, 47, 2, 61, 25,
]

suma = reduce(lambda acc, x: acc + x, numeros_4)

print(f"Lista  : {numeros_4}")
print(f"Suma   : {suma}")
print(f"Verific: {sum(numeros_4)}")


# ==============================================================================
# 5. Reduce → producto de al menos 10 enteros por un escalar
# ==============================================================================
separador("5. REDUCE — Producto de lista × escalar")

numeros_5 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
escalar = 3

producto_lista = reduce(lambda acc, x: acc * x, numeros_5)
resultado = producto_lista * escalar

print(f"Lista   : {numeros_5}")
print(f"Escalar : {escalar}")
print(f"Producto de la lista     : {producto_lista}")
print(f"Producto × escalar ({escalar}): {resultado}")


# ==============================================================================
# 6. Map + Reduce → promedio de longitud de palabras
# ==============================================================================
separador("6. MAP + REDUCE — Promedio de longitud de palabras")

palabras_6 = [
    "gato", "elefante", "hormiga", "cocodrilo", "pez",
    "mariposa", "lobo", "hipopótamo", "mosca", "tigre",
    "cóndor", "serpiente", "ratón", "rinoceronte", "abeja",
]

longitudes_6 = list(map(len, palabras_6))
suma_longitudes = reduce(lambda acc, x: acc + x, longitudes_6)
promedio = suma_longitudes / len(longitudes_6)

print(f"Palabras     : {palabras_6}")
print(f"Longitudes   : {longitudes_6}")
print(f"Suma total   : {suma_longitudes}")
print(f"Cantidad     : {len(longitudes_6)}")
print(f"Promedio     : {promedio:.2f}")


# ==============================================================================
# 7. Map + Reduce → conteo de palabras (Word Count)
# ==============================================================================
separador("7. MAP + REDUCE — Word Count")

texto_7 = [
    "hola", "mundo", "hola", "python", "mundo",
    "hola", "reduce", "map", "python", "reduce",
    "hola", "mapa", "mundo", "python", "map",
    "reduce", "hola", "python", "mundo", "map",
]

# Map: cada palabra → {palabra: 1}
pares = list(map(lambda w: {w: 1}, texto_7))

# Reduce: acumular conteos en un único diccionario
def acumular_conteo(acc, d):
    palabra, cuenta = list(d.items())[0]
    acc[palabra] = acc.get(palabra, 0) + cuenta
    return acc

conteo = reduce(acumular_conteo, pares, {})
conteo_ordenado = dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))

print(f"Texto  : {texto_7}\n")
print("Conteo por palabra:")
for palabra, count in conteo_ordenado.items():
    print(f"  {palabra:<15} → {count}")


# ==============================================================================
# 8. Reduce → promedio de notas (dataset estudiante, nota)
# ==============================================================================
separador("8. REDUCE — Promedio de notas de estudiantes")

dataset_8 = [
    ("Ana García",       8.5),
    ("Bruno López",      7.0),
    ("Carla Martínez",   9.2),
    ("Diego Fernández",  6.8),
    ("Elena Torres",     8.0),
    ("Felipe Ruiz",      5.5),
    ("Gabriela Sosa",    9.7),
    ("Hernán Díaz",      7.3),
    ("Isabel Moreno",    8.8),
    ("Javier Núñez",     6.2),
    ("Karen Pérez",      7.9),
    ("Lucía Romero",     9.1),
]

suma_notas, cantidad = reduce(
    lambda acc, alumno: (acc[0] + alumno[1], acc[1] + 1),
    dataset_8,
    (0, 0)
)
promedio_notas = suma_notas / cantidad

print(f"{'Estudiante':<25} {'Nota':>6}")
print("-" * 35)
for nombre, nota in dataset_8:
    print(f"  {nombre:<23} {nota:>6.1f}")
print("-" * 35)
print(f"  Promedio del grupo:      {promedio_notas:>6.2f}")


# ==============================================================================
# 9. Reduce → promedio, máximo y mínimo por categoría
# ==============================================================================
separador("9. REDUCE — Stats por categoría (categoría, precio)")

dataset_9 = [
    ("Electrónica",  1200.00),
    ("Ropa",           45.99),
    ("Electrónica",   350.00),
    ("Alimentos",      12.50),
    ("Ropa",           89.00),
    ("Alimentos",       5.75),
    ("Electrónica",  2500.00),
    ("Ropa",          120.00),
    ("Alimentos",      22.30),
    ("Electrónica",   480.00),
    ("Ropa",           67.50),
    ("Alimentos",       8.90),
    ("Electrónica",   990.00),
    ("Alimentos",      31.00),
    ("Ropa",           55.00),
]

def agrupar_categoria(acc, item):
    cat, precio = item
    if cat not in acc:
        acc[cat] = {"precios": [], "suma": 0, "max": precio, "min": precio}
    grupo = acc[cat]
    grupo["suma"] += precio
    grupo["precios"].append(precio)
    grupo["max"] = max(grupo["max"], precio)
    grupo["min"] = min(grupo["min"], precio)
    return acc

stats_cat = reduce(agrupar_categoria, dataset_9, {})

print(f"\n{'Categoría':<15} {'Promedio':>10} {'Máximo':>10} {'Mínimo':>10} {'Items':>6}")
print("-" * 55)
for cat, datos in sorted(stats_cat.items()):
    promedio_cat = datos["suma"] / len(datos["precios"])
    print(f"  {cat:<13} {promedio_cat:>10.2f} {datos['max']:>10.2f} {datos['min']:>10.2f} {len(datos['precios']):>6}")


# ==============================================================================
# 10. Reduce → conteo por IP y detección de IP más activa
# ==============================================================================
separador("10. REDUCE — Accesos por IP (IP, recurso, tiempo)")

dataset_10 = [
    ("192.168.1.10", "/home",     "08:01:12"),
    ("10.0.0.5",     "/login",    "08:01:45"),
    ("192.168.1.10", "/dashboard","08:02:03"),
    ("172.16.0.3",   "/api/data", "08:02:30"),
    ("10.0.0.5",     "/logout",   "08:03:01"),
    ("192.168.1.10", "/api/users","08:03:22"),
    ("10.0.0.5",     "/login",    "08:04:10"),
    ("172.16.0.3",   "/home",     "08:04:55"),
    ("192.168.1.10", "/home",     "08:05:07"),
    ("10.0.0.5",     "/api/data", "08:05:33"),
    ("192.168.1.10", "/logout",   "08:06:01"),
    ("172.16.0.3",   "/api/users","08:06:45"),
    ("10.0.0.5",     "/home",     "08:07:12"),
    ("192.168.1.10", "/login",    "08:07:50"),
    ("172.16.0.3",   "/dashboard","08:08:20"),
    ("192.168.1.10", "/api/data", "08:09:00"),
    ("10.0.0.5",     "/dashboard","08:09:30"),
    ("172.16.0.3",   "/logout",   "08:10:05"),
    ("192.168.1.10", "/home",     "08:10:45"),
    ("10.0.0.5",     "/api/users","08:11:00"),
]

def contar_accesos(acc, registro):
    ip = registro[0]
    acc[ip] = acc.get(ip, 0) + 1
    return acc

accesos_por_ip = reduce(contar_accesos, dataset_10, {})
ip_mas_activa = reduce(
    lambda a, b: a if a[1] >= b[1] else b,
    accesos_por_ip.items()
)

print(f"\n{'IP':<18} {'Accesos':>8}")
print("-" * 30)
for ip, accesos in sorted(accesos_por_ip.items(), key=lambda x: x[1], reverse=True):
    marker = " ← MÁS ACTIVA" if ip == ip_mas_activa[0] else ""
    print(f"  {ip:<16} {accesos:>8}{marker}")
