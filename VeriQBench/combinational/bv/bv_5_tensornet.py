import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(5)
    h(q[0])
    h(q[1])
    h(q[2])
    h(q[3])
    x(q[4])
    h(q[4])
    x.ctrl([q[0]], q[4])
    x.ctrl([q[1]], q[4])
    x.ctrl([q[2]], q[4])
    x.ctrl([q[3]], q[4])
    h(q[0])
    h(q[1])
    h(q[2])
    h(q[3])
    h(q[4])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)