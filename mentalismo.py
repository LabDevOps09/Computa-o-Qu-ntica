# Ideia: A densidade muda conforme a intenção (a "mente" altera a estrutura).
intencao = input("Digite a intenção (leve ou pesada): ")

if intencao == "leve":
    massa = 10  # kg
elif intencao == "pesada":
    massa = 100  # kg
else:
    massa = 50  # neutra     # qualquer valor diferente de leve ou pesado

volume = 10  # m³
densidade = massa / volume

print(f"Densidade gerada pela mente: {densidade} kg/m³")
