# Computação Quântica - Estudando

# Neurônio Quântico com Qiskit

Neste exemplo, criamos um **neurônio quântico** utilizando a biblioteca **Qiskit** e o módulo de **aprendizado de máquina quântico**. O objetivo é entender como circuitos quânticos podem ser usados para criar redes neurais quânticas (QNN), que combinam a computação clássica e quântica para resolver problemas de aprendizado de máquina. Vamos explorar o código e o que cada parte dele faz.

### 1. **Importando as bibliotecas**

Primeiro, importamos as bibliotecas necessárias para trabalhar com Qiskit e a rede neural quântica:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit_machine_learning.neural_networks import EstimatorQNN



