# Representa cada lei quântica com uma entrada física ou simbólica.
# Usa densidade, temperatura, tempo, ação, polaridade, posição geográfica e até o estado mental para ilustrar como o Universo responde ao observador.
# Interpreta os dados como estados quânticos, herméticos e simbólicos.

import math

print(" Simulador das 7 Leis Quânticas e Herméticas")
print("-" * 50)

# 1. Mentalismo — Tudo é Mente
pensamento = input("Digite um pensamento (positivo/negativo): ").lower()
if pensamento == "positivo":
    print("Mentalismo: Você colapsou a realidade para um estado de luz.")
else:
    print("Mentalismo: O colapso da realidade gerou sombra. Rumo ao equilíbrio.")

# 2. Correspondência — Como é acima, é abaixo
latitude = float(input("Digite a latitude atual: "))
longitude = float(input("Digite a longitude atual: "))
print(f"Correspondência: O micro (sua posição) espelha o macro (coordenadas da Terra) → ({latitude}, {longitude})")

# 3. Vibração — Tudo está em movimento
temperatura = float(input("Digite a temperatura em °C: "))
if temperatura < 0:
    print("Vibração: Vibração congelada. Estado quase parado.")
elif temperatura < 30:
    print("Vibração: Movimento sutil. Ritmo interno equilibrado.")
else:
    print("Vibração: Alta frequência. O sistema vibra intensamente.")

# 4. Polaridade — Tudo tem seu oposto
massa = float(input("Digite a massa (kg): "))
volume = float(input("Digite o volume (m³): "))
densidade = massa / volume

if densidade < 1:
    estado = "muito leve"
elif 1 <= densidade < 5:
    estado = "leve"
elif 5 <= densidade < 10:
    estado = "médio"
else:
    estado = "pesado"

print(f"Polaridade: Sua densidade é {densidade:.2f} kg/m³ → Estado polar: {estado}")

# 5. Ritmo — Tudo flui e reflui
tempo = float(input("Quanto tempo se passou (em segundos) desde o início do experimento? "))
fase = (tempo % (2 * math.pi))
amplitude_real = round(math.cos(fase), 3)
amplitude_imaginaria = round(math.sin(fase), 3)
print(f"Ritmo: O qubit oscilou com fase {round(fase, 3)} rad")
print(f"Amplitude real: {amplitude_real}, Amplitude imaginária: {amplitude_imaginaria}")

# 6. Causa e Efeito
acao = input("Digite uma ação (pensar/falar/fazer): ").lower()
if acao == "pensar":
    efeito = "mudança interna"
elif acao == "falar":
    efeito = "vibração externa"
else:
    efeito = "impacto físico"
print(f"Causa e Efeito: Sua ação '{acao}' causou o efeito: {efeito}")

# 7. Gênero — Tudo tem seu princípio masculino e feminino
energia = input("Digite sua energia dominante agora (ativa/receptiva): ").lower()
if energia == "ativa":
    print("Gênero: Energia masculina — expansão, ação, criação.")
else:
    print("Gênero: Energia feminina — intuição, nutrição, conexão.")

print("-" * 50)
print(" Sistema quântico simbólico completo. O Universo reagiu à sua entrada.")
