## Explicação do Código de Computação Quântica

Este código simula operações quânticas sobre dois qubits utilizando portas quânticas e realiza a medição do estado final dos qubits. As principais operações quânticas usadas são as portas **Hadamard**, **Pauli-X**, **CNOT** e uma **porta parametrizada** (dependente de um ângulo `theta`).

### Passos do código:

1. **Porta Parametrizada (Rotação):**
   - A função `porta_parametrizada(theta)` cria uma matriz de rotação, baseada no ângulo `theta`. A matriz é usada para rotacionar um qubit no plano de Bloch.

2. **Porta Hadamard:**
   - A função `hadamard()` define a matriz da porta Hadamard, que coloca um qubit em uma superposição equitativa dos estados |0⟩ e |1⟩. Essa operação é útil para introduzir incerteza nos qubits.

3. **Porta Pauli-X:**
   - A função `pauli_x()` define a matriz da porta Pauli-X, que é análoga à operação NOT, trocando os estados |0⟩ e |1⟩.

4. **Porta CNOT (Controlada):**
   - A função `cnot()` define a porta CNOT (Controlled-NOT), uma operação quântica de 2 qubits onde o primeiro qubit controla o segundo. Se o primeiro qubit está em |1⟩, o segundo qubit é invertido.

5. **Multiplicação de Matrizes:**
   - A função `multiplicar_matrizes()` realiza a multiplicação de duas matrizes, essencial para aplicar as operações quânticas nos estados dos qubits.

6. **Multiplicação de Vetor por Matriz:**
   - A função `multiplicar_vetor()` aplica uma matriz a um vetor de estado, simulando a aplicação de uma porta quântica sobre o estado do qubit.

7. **Medição dos Qubits:**
   - A função `medir()` calcula as probabilidades dos estados |00⟩, |01⟩, |10⟩ ou |11⟩, com base nos quadrados dos valores dos amplitudes de probabilidade. O código então faz uma medição probabilística para determinar o resultado, que é aleatório, mas segue as probabilidades calculadas.

### Processamento do Estado dos Qubits:

- O código inicia com o estado |00⟩ modificado para um vetor de amplitudes de probabilidade `[0.6, 0.8, 0, 0]` (superposição com diferentes pesos).
- **Rotação** é aplicada ao primeiro qubit usando a porta parametrizada com um valor de `theta = π/4`.
- **Hadamard** é aplicado ao primeiro qubit para gerar uma superposição.
- **CNOT** é aplicado, onde o primeiro qubit controla o segundo.
- O código realiza então a **medição** do estado final, convertendo o resultado em binário (ex.: `01`).

### Exemplo de Saída:
![qntest3](https://github.com/user-attachments/assets/0418dadb-87e3-4a29-bd2d-6399fa82999a)
