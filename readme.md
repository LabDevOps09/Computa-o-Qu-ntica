# Mentalismo - Conceito da Física Quântica

O conceito de **Mentalismo** na Física Quântica refere-se à ideia de que a **mente** ou a **observação** pode afetar o estado de um sistema. Em termos práticos, podemos criar uma simulação onde a "observação" ou "decisão consciente" de um observador altera o comportamento do sistema.

Em programação, podemos representar isso com um programa simples onde o estado de um sistema depende da escolha ou da observação de um "observador", refletindo a ideia de que a mente ou decisão de observar altera o comportamento do sistema.

## O Conceito

Imagine um sistema de partículas que começa em um estado **indeterminado**. A partícula pode estar em dois estados possíveis, por exemplo: "A" e "B". Quando o **observador** faz uma medição, a partícula "colapsa" em um desses estados.

### Como Representamos Isso em Código:

1. **Partícula em Estado Indeterminado**: Inicialmente, a partícula está em um estado onde ela pode estar em qualquer um dos dois estados possíveis ("A" ou "B").
2. **Observação**: A observação ou escolha do "observador" faz com que a partícula se colapse para um estado específico.
3. **Estado Final**: O estado final da partícula será aquele que o observador escolheu, mas caso o observador faça uma escolha inválida, a partícula permanecerá indeterminada.

### Como o Programa Funciona:

- **Criação da Superposição**: A partícula começa em um estado indeterminado, ou seja, ela pode estar simultaneamente em "A" e "B". Isso reflete a ideia da **superposição quântica**, onde um sistema pode estar em múltiplos estados ao mesmo tempo.
  
- **Observação**: O "observador" escolhe um dos estados ("A" ou "B"), e essa escolha colapsa a partícula para o estado escolhido. Esse processo simula o conceito de que o ato de observar ou medir influencia o estado do sistema.

- **Exibição do Estado Final**: Após a observação, o estado final da partícula é mostrado. Se o observador escolher um estado inválido, a partícula permanecerá indeterminada.

### Fluxo do Programa:

1. A partícula começa em um estado de superposição (indeterminado).
2. O observador escolhe qual estado observar (A ou B).
3. O estado da partícula é alterado de acordo com a escolha do observador, colapsando o estado quântico.

## Exemplo de Código:

Aqui está um exemplo simples de como isso pode ser implementado:

```python
import random

# Função que representa a partícula em superposição
def particula_superposicao():
    # A partícula pode estar em dois estados possíveis, A ou B
    estados_possiveis = ["A", "B"]
    return random.choice(estados_possiveis)

# Função que simula a observação
def observar_particula():
    # O observador escolhe qual estado observar
    escolha = input("Escolha um estado para observar (A ou B): ").strip().upper()
    
    # Simulação do colapso do estado baseado na escolha
    if escolha in ["A", "B"]:
        return escolha
    else:
        print("Escolha inválida. A partícula permanece indeterminada.")
        return "Indeterminado"

# Fluxo do programa
estado_particula = particula_superposicao()  # Partícula começa em superposição
print("A partícula está em superposição, ela pode estar em:", estado_particula)

# O observador faz a medição
estado_observado = observar_particula()

# Exibição do estado final
print(f"O estado final da partícula é: {estado_observado}")





