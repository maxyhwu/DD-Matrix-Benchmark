import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(3)
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    z(qubits[2])
    x.ctrl([qubits[0]], qubits[2])
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)