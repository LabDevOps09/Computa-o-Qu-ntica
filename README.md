# ⚛️ Computação Quântica - Estudando - fase inicial

# Neurônio Quântico com Qiskit

Neste exemplo, criei um **neurônio quântico** utilizando a biblioteca **Qiskit** e o módulo de **aprendizado de máquina quântico**. Vamos entender o que cada parte do código faz:

### 1. **O Circuito Quântico** ⚛️

Criei um circuito quântico simples com **2 qubits**. No circuito, apliquei duas portas principais:

- **Porta Hadamard (H)**: Essa porta é usada no primeiro qubit para criar uma **superposição**. Em termos simples, ela coloca o qubit em um estado de incerteza, ou seja, uma combinação de 0 e 1 ao mesmo tempo.

- **Porta CNOT (CX)**: A porta de controle-NOT é aplicada entre o primeiro e o segundo qubit. Ela cria um **emaranhamento** entre os qubits, o que significa que o estado de um qubit pode influenciar o estado do outro, mesmo que estejam separados por grandes distâncias. Esse fenômeno é uma das características mais fascinantes da computação quântica.

Essas operações transformam o estado inicial dos qubits em uma **superposição** entre 00, 01, 10 e 11.

### 2. **O Estimador de Estado**

Usamos o **StatevectorEstimator** do Qiskit para estimar o estado final do circuito quântico. Ele nos permite calcular o vetor de estado final do sistema quântico após as operações realizadas. O estimador pode ser visto como uma forma de medir o "resultado" do circuito, sem, no entanto, realizar uma medição direta.

### 3. **O Neurônio Quântico (QNN)** 🧠

Com o circuito quântico e o estimador configurados, criei um **Neurônio Quântico** (Quantum Neural Network - QNN). O QNN é um tipo de rede neural onde o "neurônio" é um circuito quântico. Ele utiliza as propriedades da computação quântica, como **superposição** e **emaranhamento**, para realizar o aprendizado.

No caso do nosso código, utilizamos o **EstimatorQNN** para conectar o circuito quântico ao estimador. Isso cria uma rede neural quântica simples, que poderia ser usada como base para tarefas de aprendizado de máquina, como classificação ou regressão.

### 4. **Visualizando o Circuito**

Por fim, usei o comando `qc.draw()` para visualizar o circuito quântico em uma forma gráfica. Isso nos ajuda a ver como as portas quânticas estão aplicadas e entender a estrutura do circuito de uma maneira mais intuitiva.

### 5. **Resultado Final**

Ao rodar o código, consegue visualizar o circuito, que mostra como as portas estão conectadas e como os qubits interagem ao longo do processo. O neurônio quântico que criei é uma pequena demonstração de como podemos usar a computação quântica para aplicar conceitos de aprendizado de máquina.

---

Esse exemplo é um ponto de partida para explorar mais a fundo as redes neurais quânticas e como elas podem ser aplicadas para resolver problemas complexos com a ajuda da computação quântica.

![cq](https://github.com/user-attachments/assets/163ca347-3edc-489a-900d-50b04781f1e6)



![cq2](https://github.com/user-attachments/assets/35f01554-0022-4322-90f0-4bfd8c7eb1b8)





