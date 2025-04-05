# Optimización con Metaheurísticas para Despacho Económico ⚡🧠

Este repositorio implementa tres algoritmos de optimización inspirados en la inteligencia artificial — **Algoritmo Genético (GA)**, **Particle Swarm Optimization (PSO)** y **Simulated Annealing (SA)** — aplicados al problema del **despacho económico** en sistemas eléctricos de potencia.

## 🔍 Problema

Se desea minimizar el costo total de generación eléctrica usando tres generadores, cada uno con una función de costo cuadrática:

\[
\text{Costo}_i(P_i) = a_i P_i^2 + b_i P_i + c_i
\]

### Restricciones:

- \( P_{i,\min} \leq P_i \leq P_{i,\max} \)
- \( \sum P_i = \text{Demanda} \)

---

## ⚙️ Datos del sistema

Los parámetros de los generadores son:

| Generador | a     | b    | c  | Pmin | Pmax |
|-----------|-------|------|----|------|------|
| G1        | 0.01  | 2.0  | 0  | 10   | 50   |
| G2        | 0.02  | 1.8  | 0  | 20   | 60   |
| G3        | 0.015 | 2.5  | 0  | 15   | 40   |

> **Demanda total:** 100 unidades de potencia.

---

## 📂 Archivos

- `psoga.py` → Optimización con **Algoritmo Genético (GA)**
- `pso.py`   → Optimización con **Particle Swarm Optimization (PSO)**
- `sa.py`    → Optimización con **Simulated Annealing (SA)**

Cada script es autoejecutable y muestra en consola la mejor solución y su costo asociado.

---

## ▶️ Cómo usar

### 1. Instalar Python y dependencias

```bash
pip install numpy
```

### 2. Ejecutar un script

```bash
python psoga.py
python pso.py
python sa.py
```

---

## 🧠 Metaheurísticas implementadas

### ✅ Algoritmo Genético (`psoga.py`)
- Codificación real.
- Selección por elitismo.
- Cruza lineal (blend).
- Mutación adaptativa.

### ✅ Particle Swarm Optimization (`pso.py`)
- Enjambre con 30 partículas.
- Actualización de velocidad clásica.
- Respeta restricciones físicas.

### ✅ Simulated Annealing (`sa.py`)
- Búsqueda local probabilística.
- Enfriamiento exponencial.
- Cumplimiento estricto de la demanda.

---

## 📊 Ejemplo de salida

```text
Mejor solución: [33.2, 40.5, 26.3]
Costo total: 289.73
```

---

## 📄 Licencia

MIT

---

## ✍️ Autor

Juan Esteban Rodríguez Villada – 2025  
Universidad Tecnológica de Pereira

