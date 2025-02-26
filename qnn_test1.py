from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import Statevector
from qiskit_machine_learning.neural_networks import EstimatorQNN

# Criando um circuito quântico simples
qc = QuantumCircuit(2)
qc.h(1)  # Porta Hadamard para criar superposição
qc.cx(1, 0)  # Emaranhamento entre os qubits

# Criando o Estimator atualizado
estimator = StatevectorEstimator()

# Criando a QNN corretamente
qnn = EstimatorQNN(
    circuit=qc,  # Circuito quântico usado
    estimator=estimator,  # O estimador atualizado
    input_params=[],  # Parâmetros de entrada (vazio por enquanto)
    weight_params=[]  # Parâmetros de peso (vazio por enquanto)
)

# Mostrando o circuito
print("Nosso circuito quântico:")
print(qc.draw())

# Obtendo o estado final do circuito
state = Statevector.from_instruction(qc)
print("\nEstado final dos qubits:")
print(state)  # Mostra a representação do estado quântico




