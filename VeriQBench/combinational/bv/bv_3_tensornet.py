import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(3)
    h(q[0])
    h(q[1])
    x(q[2])
    h(q[2])
    x.ctrl([q[0]], q[2])
    x.ctrl([q[1]], q[2])
    h(q[0])
    h(q[1])
    h(q[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)