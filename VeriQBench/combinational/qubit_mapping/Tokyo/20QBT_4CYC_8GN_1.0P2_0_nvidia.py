import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(20)
    x.ctrl([q[10]], q[16])
    h(q[6])
    x.ctrl([q[10]], q[9])
    y(q[9])
    h(q[16])
    y(q[9])
    x.ctrl([q[4]], q[10])
    x(q[16])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)