import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(5)
    x.ctrl([q[4]], q[1])
    x.ctrl([q[4]], q[1])
    x.ctrl([q[1]], q[3])
    x.ctrl([q[3]], q[0])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)