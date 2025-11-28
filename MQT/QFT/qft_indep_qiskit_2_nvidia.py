import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(2)
    h(q[1])
    h(q[0])
    swap(q[0], q[1])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)