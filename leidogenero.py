import math

# Estado inicial
estado = {
    "amplitude_real": 1.0,
    "amplitude_imaginaria": 0.0,
    "fase": 0
}

def aplicar_genero(estado, tipo):
    if tipo == "y":  # Ação
        estado["amplitude_real"] = 0.0
        estado["amplitude_imaginaria"] = 1.0
        estado["fase"] = math.pi / 2
    elif tipo == "x":  # Interiorização (inversão de fase)
        estado["amplitude_real"] *= -1
        estado["fase"] = math.pi
    elif tipo == "z":  # Equilíbrio fluido (π/4)
        estado["amplitude_real"] = round(math.cos(math.pi / 4), 3)
        estado["amplitude_imaginaria"] = round(math.sin(math.pi / 4), 3)
        estado["fase"] = round(math.pi / 4, 3)

    return estado

# Exibindo os três estados
print(" Estado inicial:")
print(estado)

print("\n Aplicando princípio y (masculino):")
print(aplicar_genero(estado.copy(), "y"))

print("\n Aplicando princípio x (feminino):")
print(aplicar_genero(estado.copy(), "x"))

print("\n Aplicando princípio z (mutável):")
print(aplicar_genero(estado.copy(), "z"))
