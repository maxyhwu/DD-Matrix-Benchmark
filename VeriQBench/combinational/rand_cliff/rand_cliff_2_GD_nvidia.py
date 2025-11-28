import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(2)
    s(q[0])
    h(q[0])
    s(q[1])
    swap(q[1], q[0])
    x.ctrl([q[1]], q[0])
    h(q[0])
    x.ctrl([q[0]], q[1])
    z(q[0])
    z(q[1])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)