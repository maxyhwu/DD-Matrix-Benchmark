import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(7)
    h(qubits[0])
    x.ctrl([qubits[0]], qubits[1])
    x.ctrl([qubits[1]], qubits[2])
    x.ctrl([qubits[2]], qubits[3])
    x.ctrl([qubits[3]], qubits[4])
    x.ctrl([qubits[4]], qubits[5])
    x.ctrl([qubits[5]], qubits[6])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)