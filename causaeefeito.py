import math

# Estado do qubit
qubit = {
    'amplitude_real': 1.0,
    'amplitude_imaginaria': 0.0,
    'fase': 0
}

def aplicar_causa(fase_incremento, estado):
    estado['fase'] += fase_incremento
    estado['amplitude_real'] = round(math.cos(estado['fase']), 3)
    estado['amplitude_imaginaria'] = round(math.sin(estado['fase']), 3)
    return estado

print("🔵 Estado inicial:")
print(qubit)

# Causa 1: aplicar π/6 (30 graus)
print("\n Causa 1: Vibração +π/6 (30°)...")
qubit = aplicar_causa(math.pi / 6, qubit)
print(" Efeito 1:", qubit)

# Causa 2: usar o efeito anterior como base e aplicar +π/3 (60°)
print("\n Causa 2: Vibração +π/3 (60°)...")
qubit = aplicar_causa(math.pi / 3, qubit)
print(" Efeito 2:", qubit)

# Causa 3: inverter movimento (–π/2)
print("\n Causa 3: Vibração reversa -π/2 (90°)...")
qubit = aplicar_causa(-math.pi / 2, qubit)
print(" Efeito 3:", qubit)

print("\n🔁 Fim da cadeia de causas e efeitos.")
