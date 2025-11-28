import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(6)
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    h(qubits[3])
    h(qubits[4])
    h(qubits[5])
    z(qubits[5])
    x.ctrl([qubits[0]], qubits[5])
    x.ctrl([qubits[2]], qubits[5])
    x.ctrl([qubits[4]], qubits[5])
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    h(qubits[3])
    h(qubits[4])
    h(qubits[5])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)