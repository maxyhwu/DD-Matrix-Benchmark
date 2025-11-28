import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(5)
    x.ctrl([q[3]], q[4])
    x.ctrl([q[3]], q[4])
    x.ctrl([q[3]], q[4])
    x.ctrl([q[3]], q[4])
    x.ctrl([q[4]], q[2])
    x.ctrl([q[2]], q[1])
    x.ctrl([q[2]], q[1])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[2]], q[1])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[2]], q[4])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)