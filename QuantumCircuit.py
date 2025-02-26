from qiskit import Aer, execute, QuantumCircuit

# Criando um circuito quântico com 1 qubit
qc = QuantumCircuit(1)

# Adicionando uma porta Hadamard para criar uma superposição
qc.h(0)

# Medindo o qubit
qc.measure_all()

# Escolhendo o simulador
simulator = Aer.get_backend('qasm_simulator')

# Executando o circuito no simulador
job = execute(qc, simulator, shots=1000)

# Pegando os resultados
result = job.result()
counts = result.get_counts(qc)

# Exibindo os resultados
print("Resultados da medição:", counts)









