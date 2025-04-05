import numpy as np
import random

# Parámetros
generadores = [
    {"a": 0.01, "b": 2.0, "c": 0, "Pmin": 10, "Pmax": 50},
    {"a": 0.02, "b": 1.8, "c": 0, "Pmin": 20, "Pmax": 60},
    {"a": 0.015, "b": 2.5, "c": 0, "Pmin": 15, "Pmax": 40},
]
DEMANDA = 100

def costo_total(P):
    if abs(sum(P) - DEMANDA) > 1e-2:
        return 1e6
    return sum(g["a"]*P[i]**2 + g["b"]*P[i] + g["c"] for i, g in enumerate(generadores))

def crear_individuo():
    P = [random.uniform(g["Pmin"], g["Pmax"]) for g in generadores]
    factor = DEMANDA / sum(P)
    return [p * factor for p in P]

def mutar(P):
    i = random.randint(0, 2)
    delta = random.uniform(-1, 1)
    P[i] = np.clip(P[i] + delta, generadores[i]["Pmin"], generadores[i]["Pmax"])
    factor = DEMANDA / sum(P)
    return [p * factor for p in P]

def cruzar(p1, p2):
    alpha = random.random()
    P = [alpha * p1[i] + (1 - alpha) * p2[i] for i in range(3)]
    factor = DEMANDA / sum(P)
    return [p * factor for p in P]

# Algoritmo genético
poblacion = [crear_individuo() for _ in range(30)]

for gen in range(100):
    poblacion.sort(key=costo_total)
    nueva_pob = poblacion[:10]  # elitismo
    while len(nueva_pob) < 30:
        p1, p2 = random.sample(poblacion[:20], 2)
        hijo = cruzar(p1, p2)
        hijo = mutar(hijo)
        nueva_pob.append(hijo)
    poblacion = nueva_pob

mejor = min(poblacion, key=costo_total)
print("Mejor solución:", mejor)
print("Costo total:", costo_total(mejor))
