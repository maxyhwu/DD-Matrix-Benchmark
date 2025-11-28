import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(6)
    h(q[5])
    h(q[4])
    h(q[3])
    h(q[2])
    h(q[1])
    h(q[0])
    swap(q[0], q[5])
    swap(q[1], q[4])
    swap(q[2], q[3])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)