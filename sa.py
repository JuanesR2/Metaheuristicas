import numpy as np
import random
import math

generadores = [
    {"a": 0.01, "b": 2.0, "c": 0, "Pmin": 10, "Pmax": 50},
    {"a": 0.02, "b": 1.8, "c": 0, "Pmin": 20, "Pmax": 60},
    {"a": 0.015, "b": 2.5, "c": 0, "Pmin": 15, "Pmax": 40},
]
DEMANDA = 100

def costo(P):
    if abs(sum(P) - DEMANDA) > 1e-2:
        return 1e6
    return sum(g["a"]*P[i]**2 + g["b"]*P[i] + g["c"] for i, g in enumerate(generadores))

def vecino(P):
    i = random.randint(0, 2)
    P_new = P.copy()
    P_new[i] += random.uniform(-1, 1)
    P_new[i] = np.clip(P_new[i], generadores[i]["Pmin"], generadores[i]["Pmax"])
    factor = DEMANDA / sum(P_new)
    return [p * factor for p in P_new]

P = [random.uniform(g["Pmin"], g["Pmax"]) for g in generadores]
P = [p * DEMANDA / sum(P) for p in P]
T = 100.0
best = P
best_cost = costo(P)

for _ in range(1000):
    P_new = vecino(P)
    delta = costo(P_new) - costo(P)
    if delta < 0 or random.random() < math.exp(-delta / T):
        P = P_new
        if costo(P) < best_cost:
            best = P
            best_cost = costo(P)
    T *= 0.99  # Enfriamiento

print("Mejor solución:", best)
print("Costo total:", best_cost)
