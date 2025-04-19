import math
import matplotlib.pyplot as plt

# Estado inicial do qubit: |0⟩
estado = {
    "amplitude_real": 1.0,
    "amplitude_imaginaria": 0.0,
    "fase": 0
}

def aplicar_porta_x(estado):
    print("Aplicando Porta X (inversão de polaridade)...")
    estado["amplitude_real"] = 0.0
    estado["amplitude_imaginaria"] = 1.0
    estado["fase"] = math.pi / 2  # 90°
    return estado

def aplicar_porta_z(estado):
    print("Aplicando Porta Z (inversão de fase)...")
    estado["amplitude_real"] *= -1  # Inverte a fase no eixo real
    estado["fase"] = math.pi  # 180°
    return estado

def aplicar_porta_y(estado):
    print("Aplicando Porta Y (giro imaginário)...")
    estado["amplitude_real"] = 1 / math.sqrt(2)
    estado["amplitude_imaginaria"] = -1 / math.sqrt(2)
    estado["fase"] = -math.pi / 4  # -45°
    return estado

def mostrar_estado(titulo, estado, cor):
    print(f"{titulo}")
    print({
        "amplitude_real": round(estado['amplitude_real'], 3),
        "amplitude_imaginaria": round(estado['amplitude_imaginaria'], 3),
        "fase": round(estado['fase'], 6)
    })

    # Desenhar gráfico
    plt.arrow(0, 0, estado['amplitude_real'], estado['amplitude_imaginaria'],
              head_width=0.05, color=cor, length_includes_head=True)
    plt.text(estado['amplitude_real'] + 0.05, estado['amplitude_imaginaria'],
             titulo, color=cor, fontsize=9)

# Plot
plt.figure(figsize=(5, 5))
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)

# Estados
mostrar_estado("|0⟩", estado, 'blue')

estado_x = aplicar_porta_x(estado.copy())
mostrar_estado("|1⟩ (X)", estado_x, 'red')

estado_z = aplicar_porta_z(estado.copy())
mostrar_estado("Z aplicada", estado_z, 'green')

estado_y = aplicar_porta_y(estado.copy())
mostrar_estado("Y aplicada", estado_y, 'purple')

plt.title("Lei da Polaridade — Qubit em Movimento")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
