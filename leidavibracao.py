# Representar a vibração como oscilação angular.

import math

angulo = math.pi / 6  # 30 graus
velocidade = 20  # m/s

frequencia = velocidade * math.sin(angulo)
print(f"Frequência vibracional: {round(frequencia, 2)} Hz")
