# Mentalismo - Conceito da Física Quântica

O conceito de **Mentalismo** na Física Quântica refere-se à ideia de que a **mente** ou a **observação** pode afetar o estado de um sistema. Em termos práticos, pode se criar uma simulação onde a "observação" ou "decisão consciente" de um observador altera o comportamento do sistema.

Em programação, pode representar isso com um programa simples onde o estado de um sistema depende da escolha ou da observação de um "observador", refletindo a ideia de que a mente ou decisão de observar altera o comportamento do sistema.

## O Conceito

Imagine um sistema de partículas que começa em um estado **indeterminado**. A partícula pode estar em dois estados possíveis, por exemplo: "A" e "B". Quando o **observador** faz uma medição, a partícula "colapsa" em um desses estados.

### Como Representamos Isso em Código:

1. **Partícula em Estado Indeterminado**: Inicialmente, a partícula está em um estado onde ela pode estar em qualquer um dos dois estados possíveis ("A" ou "B").
2. **Observação**: A observação ou escolha do "observador" faz com que a partícula se colapse para um estado específico.
3. **Estado Final**: O estado final da partícula será aquele que o observador escolheu, mas caso o observador faça uma escolha inválida, a partícula permanecerá indeterminada.

- **Exibição do Estado Final**: Após a observação, o estado final da partícula é mostrado. Se o observador escolher um estado inválido, a partícula permanecerá indeterminada.

### Fluxo do Programa:

1. A partícula começa em um estado de superposição (indeterminado).
2. O observador escolhe qual estado observar (A ou B).
3. O estado da partícula é alterado de acordo com a escolha do observador, colapsando o estado quântico.
   
Estado_particula = particula_superposicao()  # Partícula começa em superposição
print("A partícula está em superposição, ela pode estar em:", estado_particula)

# O observador faz a medição
estado_observado = observar_particula()

# Exibição do estado final
print(f"O estado final da partícula é: {estado_observado}")



![quantic](https://github.com/user-attachments/assets/d15b2703-b565-4320-a147-9d05b2db05bc)


