import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    qubits = cudaq.qvector(2)
    h(qubits[0])
    x.ctrl([qubits[0]], qubits[1])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)