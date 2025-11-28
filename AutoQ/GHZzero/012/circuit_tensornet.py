import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(12)
    h(qubits[0])
    x.ctrl([qubits[0]], qubits[1])
    x.ctrl([qubits[1]], qubits[2])
    x.ctrl([qubits[2]], qubits[3])
    x.ctrl([qubits[3]], qubits[4])
    x.ctrl([qubits[4]], qubits[5])
    x.ctrl([qubits[5]], qubits[6])
    x.ctrl([qubits[6]], qubits[7])
    x.ctrl([qubits[7]], qubits[8])
    x.ctrl([qubits[8]], qubits[9])
    x.ctrl([qubits[9]], qubits[10])
    x.ctrl([qubits[10]], qubits[11])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)