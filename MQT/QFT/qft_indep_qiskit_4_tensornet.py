import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(4)
    h(q[3])
    h(q[2])
    h(q[1])
    h(q[0])
    swap(q[0], q[3])
    swap(q[1], q[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)