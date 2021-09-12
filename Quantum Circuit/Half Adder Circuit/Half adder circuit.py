from qiskit import QuantumCircuit, assemble, Aer, execute
from qiskit.visualization import plot_histogram

# To add 1 and 1

#Intialize 4 qubits and 2 bits
circ = QuantumCircuit(4, 2)
#Applying X gate on 1st and 2nd qubit
circ.x(0)
circ.x(1)
#Putting a barrier
circ.barrier()
#Applying cnot gate from qubit 1 to 3 and from qubit 2 to 3
circ.cx(0,2)
circ.cx(1,2)
#Applying toffoli gate
circ.ccx(0,1,3)
circ.barrier()
circ.measure(2,0) #Extract XOR value
circ.measure(3,1) #Extract AND value
circ.draw()

#Running on a simulator
sim = Aer.get_backend('qasm_simulator')
job = execute(circ, sim, shots = 1000)
result = job.result()
counts = result.get_counts(circ)
plot_histogram(counts)


# To add 0 and 0
a = QuantumCircuit(4,2)
a.barrier()
a.cx(0,1)
a.cx(1,2)
a.ccx(0,1,3)
a.barrier()
a.measure(2,0)
a.measure(3,1)
a.draw()
sim = Aer.get_backend('qasm_simulator')
job = execute(a, sim, shots = 1000)
result = job.result()
counts = result.get_counts(a)
plot_histogram(counts)


# To add 1 and 0
b = QuantumCircuit(4,2)
b.x(0)
b.barrier()
b.cx(0,1)
b.cx(1,2)
b.ccx(0,1,3)
b.barrier()
b.measure(2,0)
b.measure(3,1)
b.draw()
sim = Aer.get_backend('qasm_simulator')
job = execute(b, sim, shots = 1000)
result = job.result()
counts = result.get_counts(b)
plot_histogram(counts)


# To add 0 and 1
c = QuantumCircuit(4,2)
c.x(1)
c.barrier()
c.cx(0,1)
c.cx(1,2)
c.ccx(0,1,3)
c.barrier()
c.measure(2,0)
c.measure(3,1)
c.draw()
sim = Aer.get_backend('qasm_simulator')
job = execute(c, sim, shots = 1000)
result = job.result()
counts = result.get_counts(c)
plot_histogram(counts)

