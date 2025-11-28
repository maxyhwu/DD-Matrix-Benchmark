import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(3)
    s(q[0])
    h(q[0])
    s(q[0])
    x.ctrl([q[0]], q[2])
    x.ctrl([q[0]], q[1])
    h(q[1])
    x.ctrl([q[1]], q[0])
    s(q[1])
    s(q[2])
    h(q[2])
    z(q[1])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)