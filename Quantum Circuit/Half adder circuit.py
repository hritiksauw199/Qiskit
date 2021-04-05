from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

# To add 1 and 1

#Intialize 4 qubits and 2 bits
a = QuantumCircuit(4, 2)
#Applying X gate on 1st and 2nd qubit
a.x(0)
a.x(1)
#Putting a barrier
a.barrier()
#Applying cnot gate from qubit 1 to 3 and from qubit 2 to 3
a.cx(0,2)
a.cx(1,2)
#Applying toffoli gate
a.ccx(0,1,3)
a.barrier()
a.measure(2,0) #Extract XOR value
a.measure(3,1) #Extract AND value
a.draw()

#Running on a simulator
sim = Aer.get_backend('qasm_simulator')
obj = assemble(a)
result = sim.run(obj).result()
counts = result.get_counts()
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
qobj = assemble(a)
result = sim.run(qobj).result()
counts = result.get_counts()
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
qobj = assemble(b)
result = sim.run(qobj).result()
counts = result.get_counts()
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
qobj = assemble(c)
result = sim.run(qobj).result()
counts = result.get_counts()
plot_histogram(counts)

