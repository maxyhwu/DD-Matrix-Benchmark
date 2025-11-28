import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(9)
    h(q[8])
    h(q[7])
    h(q[6])
    h(q[5])
    h(q[4])
    h(q[3])
    h(q[2])
    h(q[1])
    h(q[0])
    swap(q[0], q[8])
    swap(q[1], q[7])
    swap(q[2], q[6])
    swap(q[3], q[5])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)