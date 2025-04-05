import numpy as np

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

# Inicialización
n_particulas = 30
pos = np.array([[np.random.uniform(g["Pmin"], g["Pmax"]) for g in generadores] for _ in range(n_particulas)])
for i in range(n_particulas):
    factor = DEMANDA / sum(pos[i])
    pos[i] *= factor

vel = np.zeros_like(pos)
pbest = pos.copy()
pbest_val = np.array([costo(p) for p in pbest])
gbest = pbest[np.argmin(pbest_val)]

# PSO loop
for _ in range(100):
    r1, r2 = np.random.rand(), np.random.rand()
    vel = 0.5*vel + 1.5*r1*(pbest - pos) + 1.5*r2*(gbest - pos)
    pos += vel
    for i in range(n_particulas):
        pos[i] = np.clip(pos[i], [g["Pmin"] for g in generadores], [g["Pmax"] for g in generadores])
        pos[i] *= DEMANDA / sum(pos[i])  # Cumplir restricción
        val = costo(pos[i])
        if val < pbest_val[i]:
            pbest[i] = pos[i]
            pbest_val[i] = val
    gbest = pbest[np.argmin(pbest_val)]

print("Mejor solución:", gbest)
print("Costo total:", costo(gbest))
