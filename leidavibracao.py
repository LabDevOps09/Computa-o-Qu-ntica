import math
import time

# Estado inicial (representado em "fase zero")
estado_qubit = {
    "amplitude_real": 1.0,
    "amplitude_imaginaria": 0.0,
    "fase": 0  # Em radianos
}

def vibrar_qubit(estado, angulo):
    """Aplica uma vibração (mudança de fase) ao qubit"""
    nova_fase = estado["fase"] + angulo
    estado["fase"] = nova_fase
    estado["amplitude_real"] = round(math.cos(nova_fase), 3)
    estado["amplitude_imaginaria"] = round(math.sin(nova_fase), 3)
    return estado

# Exibição inicial
print("Estado inicial do qubit:")
print(estado_qubit)

# Simulando a vibração (aplicando fase π/3)
print("\nAplicando vibração (fase π/3)...")
time.sleep(1)

estado_qubit = vibrar_qubit(estado_qubit, math.pi/3)

# Exibindo novo estado
print("\nNovo estado do qubit após vibração:")
print(estado_qubit)
