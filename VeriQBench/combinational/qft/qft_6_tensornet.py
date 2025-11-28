import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(6)
    h(q[0])
    h(q[1])
    h(q[2])
    h(q[3])
    h(q[4])
    h(q[5])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)