import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(4)
    x.ctrl([q[1], q[2]], q[3])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[0], q[2]], q[3])
    x.ctrl([q[0]], q[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)