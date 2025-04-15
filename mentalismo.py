import random

class SistemaMentalismo:
    def __init__(self):
        # Inicializa o sistema com a partícula em estado indeterminado
        self.estado = None
    
    def criar_superposicao(self):
        # A partícula está em um estado de superposição (ambos A e B simultaneamente)
        self.estado = "indeterminado"
        print("A partícula está em superposição: Estado indeterminado (A e B ao mesmo tempo)")
    
    def observacao(self, escolha_observador):
        # O observador escolhe um estado, que "colapsa" a superposição
        if escolha_observador == "A":
            self.estado = "A"
            print("Observador escolheu: A. A partícula colapsou para o estado A.")
        elif escolha_observador == "B":
            self.estado = "B"
            print("Observador escolheu: B. A partícula colapsou para o estado B.")
        else:
            print("Escolha inválida. A partícula permanece indeterminada.")
    
    def mostrar_estado(self):
        # Mostra o estado atual da partícula
        if self.estado == "indeterminado":
            print("A partícula ainda está em superposição (indeterminada).")
        else:
            print(f"A partícula está no estado {self.estado}.")

# Exemplo de uso
sistema = SistemaMentalismo()

# 1. Criar a superposição (estado indeterminado)
sistema.criar_superposicao()

# 2. O observador faz uma escolha (A ou B)
escolha = input("Escolha o estado que deseja observar (A ou B): ").upper()
sistema.observacao(escolha)

# 3. Mostrar o estado final
sistema.mostrar_estado()
