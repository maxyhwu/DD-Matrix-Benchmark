import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(3)
    x(qubits[0])
    z.ctrl([qubits[0]], qubits[1])
    x(qubits[0])
    h(qubits[0])
    h(qubits[1])
    x(qubits[0])
    x(qubits[1])
    z.ctrl([qubits[0]], qubits[1])
    x(qubits[0])
    x(qubits[1])
    h(qubits[0])
    h(qubits[1])
    z(qubits[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)