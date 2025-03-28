import random

# Função para a porta Hadamard
def hadamard():
    return [[1/2**0.5, 1/2**0.5], [1/2**0.5, -1/2**0.5]]

# Função para a porta Pauli-X
def pauli_x():
    return [[0, 1], [1, 0]]

# Função para a porta CNOT
def cnot():
    return [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]

# Multiplicação de matrizes
def multiplicar_matrizes(A, B):
    linhas_A, colunas_A = len(A), len(A[0])
    linhas_B, colunas_B = len(B), len(B[0])

    if colunas_A != linhas_B:
        raise ValueError("Matrizes incompatíveis para multiplicação.")

    resultado = [[0] * colunas_B for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

# Multiplicação de vetor por matriz
def multiplicar_vetor(matriz, vetor):
    resultado = [0] * len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resultado[i] += matriz[i][j] * vetor[j]
    return resultado

# Medição de qubits
def medir(estado):
    probabilidades = [abs(x)**2 for x in estado]
    total_prob = sum(probabilidades)
    probabilidades = [p / total_prob for p in probabilidades]

    # Escolhe um estado baseado nas probabilidades
    valor_aleatorio = random.random()
    prob_acumulada = 0.0
    for i, prob in enumerate(probabilidades):
        prob_acumulada += prob
        if valor_aleatorio <= prob_acumulada:
            return i

# Estado inicial |00>
estado_2qubits = [1, 0, 0, 0]  # Representação de |00>

# Aplicando Hadamard no primeiro qubit
H = hadamard()
H_expandido = [[H[0][0], H[0][1], 0, 0], [H[1][0], H[1][1], 0, 0], [0, 0, H[0][0], H[0][1]], [0, 0, H[1][0], H[1][1]]]
estado_2qubits = multiplicar_vetor(H_expandido, estado_2qubits)

# Aplicando CNOT
CNOT = cnot()
estado_2qubits = multiplicar_vetor(CNOT, estado_2qubits)

# Medindo os estados dos dois qubits corretamente
medicao = medir(estado_2qubits)
resultado_binario = format(medicao, '02b')  # Converte para binário (exemplo: '10')

print(f"Resultado da medição: {resultado_binario}")
