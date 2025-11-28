import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(6)
    x.ctrl([qubits[0], qubits[1]], qubits[2])
    x.ctrl([qubits[3], qubits[2]], qubits[4])
    x.ctrl([qubits[4]], qubits[5])
    x.ctrl([qubits[3], qubits[2]], qubits[4])
    x.ctrl([qubits[0], qubits[1]], qubits[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)