import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(54)
    z(q[50])
    t(q[35])
    x.ctrl([q[50]], q[8])
    z(q[50])
    x(q[51])
    t(q[50])
    x.ctrl([q[10]], q[25])
    x.ctrl([q[32]], q[1])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)