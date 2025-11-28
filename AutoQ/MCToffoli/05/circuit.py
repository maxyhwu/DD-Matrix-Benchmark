import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(10)
    x.ctrl([qubits[0], qubits[1]], qubits[2])
    x.ctrl([qubits[3], qubits[2]], qubits[4])
    x.ctrl([qubits[5], qubits[4]], qubits[6])
    x.ctrl([qubits[7], qubits[6]], qubits[8])
    x.ctrl([qubits[8]], qubits[9])
    x.ctrl([qubits[7], qubits[6]], qubits[8])
    x.ctrl([qubits[5], qubits[4]], qubits[6])
    x.ctrl([qubits[3], qubits[2]], qubits[4])
    x.ctrl([qubits[0], qubits[1]], qubits[2])

    counts = cudaq.sample(circuit, shots_count=1024)
    print(counts)