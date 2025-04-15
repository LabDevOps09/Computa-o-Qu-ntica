import random

class Emaranhamento:
    def __init__(self):
        # Inicializa as partículas em estado "não definido"
        self.particula_A = None
        self.particula_B = None
        self.estado_inicial = None

    def gerar_emaranhamento(self):
        # Criamos uma superposição inicial de 50% para 0 ou 1 para cada partícula
        estados_possiveis = [0, 1]
        self.estado_inicial = random.choice(estados_possiveis)
        self.particula_A = self.estado_inicial
        self.particula_B = self.estado_inicial
        print("Partículas A e B foram emaranhadas no estado inicial (A=B):", self.estado_inicial)
    
    def medir(self):
        # O "observador" mede a partícula A, o que imediatamente afeta a partícula B devido ao emaranhamento
        if self.particula_A == 0:
            self.particula_B = 0
        else:
            self.particula_B = 1
        print(f"Medindo a partícula A: {self.particula_A}")
        print(f"Partícula A colapsou para o estado: {self.particula_A}")
        print(f"Partícula B, distante, colapsou para o mesmo estado devido ao emaranhamento: {self.particula_B}")
    
    def mostrar_estados(self):
        print("Estado final das partículas:")
        print(f"Partícula A: {self.particula_A}")
        print(f"Partícula B: {self.particula_B}")

# Exemplo de uso
sistema = Emaranhamento()

# 1. Criamos o emaranhamento
sistema.gerar_emaranhamento()

# 2. O "observador" mede a partícula A, afetando imediatamente a partícula B
sistema.medir()

# 3. Mostrar os estados finais das partículas
sistema.mostrar_estados()
