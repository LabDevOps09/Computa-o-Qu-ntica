from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit_machine_learning.neural_networks import EstimatorQNN

# Criando um circuito quântico simples
qc = QuantumCircuit(2)
qc.h(0)  # Porta Hadamard para criar superposição
qc.cx(0, 1)  # Emaranhamento entre os qubits

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
print(qc.draw())


