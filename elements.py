import math

print("Simulador Quântico dos Elementos da Terra")
print("-" * 50)

# 1. Mentalismo — Tudo é Mente
agua = input("Escolha seu estado de água interior (calma/turbulenta): ").lower()
if agua == "calma":
    print("Mentalismo: A água reflete clareza mental. Realidade iluminada.")
else:
    print("Mentalismo: A água turbulenta indica confusão e aprendizado em processo.")

# 2. Correspondência — Como é acima, é abaixo
terra = input("Sinta a estabilidade da terra (firme/mole): ").lower()
if terra == "firme":
    print("Correspondência: Seu microcosmo está alinhado com o macrocosmo.")
else:
    print("Correspondência: Há desequilíbrio. Busque harmonia com o todo.")

# 3. Vibração — Tudo está em movimento
vento = input("Quão rápido sopra o vento ao seu redor (fraco/forte): ").lower()
if vento == "fraco":
    print("Vibração: Baixa frequência. Movimento sutil.")
else:
    print("Vibração: Alta frequência. O sistema vibra intensamente.")

# 4. Polaridade — Tudo tem seu oposto
fogo = input("Escolha a intensidade do fogo (frio/quente): ").lower()
if fogo == "frio":
    estado = "energia receptiva"
else:
    estado = "energia ativa"
print(f"Polaridade: O fogo simboliza sua polaridade → {estado}")

# 5. Ritmo — Tudo flui e reflui
maré = float(input("Digite a altura atual da maré ou fluxo do vento (em metros): "))
fase = (maré % (2 * math.pi))
amplitude_real = round(math.cos(fase), 3)
amplitude_imaginaria = round(math.sin(fase), 3)
print(f"Ritmo: O fluxo oscilou com fase {round(fase, 3)} rad")
print(f"Amplitude real: {amplitude_real}, Amplitude imaginária: {amplitude_imaginaria}")

# 6. Causa e Efeito — Ação gera reação
gravidade = input("Você lançou uma ação (movimento/pensamento/fala): ").lower()
if gravidade == "pensamento":
    efeito = "reflexo interno"
elif gravidade == "fala":
    efeito = "eco externo"
else:
    efeito = "impacto físico"
print(f"Causa e Efeito: Sua ação '{gravidade}' gerou → {efeito}")

# 7. Gênero — Tudo tem seu princípio masculino e feminino
ar = input("Qual energia predomina em você agora (ativa/receptiva): ").lower()
if ar == "ativa":
    print("Gênero: Energia masculina — expansão, ação, criação.")
else:
    print("Gênero: Energia feminina — intuição, nutrição, conexão.")

print("-" * 50)
print("Sistema quântico simbólico dos elementos completo. O Universo reagiu às suas escolhas.")
