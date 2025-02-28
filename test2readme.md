# Explicação do Código

Este código implementa uma sequência simples de operações em computação quântica, com foco em manipulação de estados quânticos de dois qubits. Ele utiliza portas quânticas como Hadamard, Pauli-X e CNOT, além de realizar a multiplicação de matrizes e vetores, e a medição dos estados finais dos qubits.

## 1. Porta Hadamard
A **porta Hadamard** é uma das operações mais importantes em computação quântica. Quando aplicada a um qubit, ela cria uma superposição de estados, ou seja, transforma o estado |0> em uma combinação igual de |0> e |1>. A aplicação dessa porta no primeiro qubit do sistema cria uma superposição entre os dois qubits.

## 2. Porta Pauli-X
A **porta Pauli-X** é uma operação de inversão, similar à operação de "NOT" na computação clássica. Ela troca os estados |0> e |1>. Embora o código não utilize essa porta diretamente no exemplo, ela é uma das portas quânticas mais comuns e pode ser aplicada a qubits para inverter seu estado.

## 3. Porta CNOT (Controlled-NOT)
A **porta CNOT** é uma porta quântica de dois qubits. Ela realiza uma operação condicional: o segundo qubit (chamado de "alvo") será invertido se o primeiro qubit (chamado de "controle") estiver no estado |1>. Se o primeiro qubit estiver no estado |0>, o segundo qubit não é alterado.

## 4. Multiplicação de Matrizes
O código implementa uma função para multiplicação de matrizes, que é usada para aplicar as operações das portas quânticas aos estados dos qubits. As portas quânticas podem ser representadas por matrizes, e multiplicá-las pelos vetores de estado dos qubits atualiza o estado do sistema.

## 5. Multiplicação de Vetor por Matriz
Além da multiplicação de matrizes, o código também inclui uma função para multiplicar um vetor por uma matriz. Essa operação é usada para aplicar as portas quânticas aos estados dos qubits, alterando o vetor de estado do sistema.

## 6. Medição dos Qubits
Após aplicar as portas quânticas, o estado final dos qubits é medido. A medição quântica é uma das características fundamentais da computação quântica. Ela envolve a probabilidade de se observar um determinado estado quando o sistema é medido. O código simula essa medição e escolhe um dos estados possíveis com base nas probabilidades associadas a cada um.

## 7. Resultado Final
O código imprime o resultado da medição, que será um valor binário representando o estado observado dos dois qubits após as operações.

## Conclusão
Este código é um exemplo simples de como aplicar operações quânticas, como a Hadamard e CNOT, em um sistema de dois qubits. Ele também demonstra como realizar medições probabilísticas de estados quânticos. Embora simples, ele serve como uma boa introdução à manipulação de qubits e à computação quântica em geral. 

**Obs** A ideia era criar um circuito quântico sem importar bibliotecas. (bem díficil, e ainda continuarei trabalhando nesse código (rs))

![cq1](https://github.com/user-attachments/assets/9bddc9cd-5d00-4e2a-b028-8e4928a76a4a)


![cq2](https://github.com/user-attachments/assets/d0a7b181-b9b3-4eda-8367-023a92a97c97)

![cq](https://github.com/user-attachments/assets/9abb85d2-0456-4d19-b1ed-ab7947de7437)


