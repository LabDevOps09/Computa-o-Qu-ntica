# Ideia: Se a densidade for maior que X, o sistema está em “pesado”; senão, “leve”.
massa = float(input("Digite a massa (kg): "))
volume = float(input("Digite o volume (m³): "))

densidade = massa / volume

estado = "leve" if densidade < 2 else "pesado"
print(f"Densidade: {densidade} kg/m³ → Estado polar: {estado}")
