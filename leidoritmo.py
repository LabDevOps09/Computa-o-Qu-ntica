import math

# Estado inicial
qubit = {
    "amplitude_real": 1.0,
    "amplitude_imaginaria": 0.0,
    "fase": 0
}
def aplicar_fase(qubit, angulo_rad):
    qubit["fase"] += angulo_rad
    qubit["amplitude_real"] = round(math.cos(qubit["fase"]), 3)
    qubit["amplitude_imaginaria"] = round(math.sin(qubit["fase"]), 3)
    return qubit
print(" Início do ciclo quântico - Lei do Ritmo ")
print("🔵 Estado inicial:")
print(qubit)

# Sobe (ângulo π/4 → 45°)
print("\n⏫ Subindo vibração (+π/4)...")
aplicar_fase(qubit, math.pi/4)
print(qubit)

# Mais subida (ângulo π/4 → agora soma +π/4, total π/2 → 90°)
print("\n⏫ Mais vibração (+π/4)...")
aplicar_fase(qubit, math.pi/4)
print(qubit)

# Desce (ângulo -π/2 → volta ao ponto inicial)
print("\n⏬ Descendo (-π/2)...")
aplicar_fase(qubit, -math.pi/2)
print(qubit)

print("\n Fim do ciclo - o ritmo completou sua volta.")
