# Ideia: Uma massa sobe e desce num movimento cíclico (ex: pêndulo com ângulo)
import math

fase = 0
for i in range(4):
    altura = round(math.sin(fase) * 5, 2)
    print(f"Ciclo {i+1} → Altura: {altura}m")
    fase += math.pi / 4
