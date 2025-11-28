import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(5)
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    h(qubits[3])
    h(qubits[4])
    z(qubits[4])
    x.ctrl([qubits[0]], qubits[4])
    x.ctrl([qubits[2]], qubits[4])
    h(qubits[0])
    h(qubits[1])
    h(qubits[2])
    h(qubits[3])
    h(qubits[4])

    counts = cudaq.sample(circuit, shots_count=1024)
    print(counts)