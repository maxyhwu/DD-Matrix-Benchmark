import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(16)
    y(q[2])
    x.ctrl([q[0]], q[3])
    h(q[2])
    x.ctrl([q[10]], q[8])
    y(q[13])
    x.ctrl([q[4]], q[9])
    x.ctrl([q[2]], q[5])
    t(q[5])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)