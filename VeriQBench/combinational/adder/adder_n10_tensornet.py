import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(10)
    x.ctrl([q[1], q[2]], q[3])
    x.ctrl([q[1]], q[2])
    x.ctrl([q[4], q[5]], q[6])
    x.ctrl([q[4]], q[5])
    x.ctrl([q[7], q[8]], q[9])
    x.ctrl([q[7]], q[8])
    x.ctrl([q[0], q[2]], q[3])
    x.ctrl([q[3], q[5]], q[6])
    x.ctrl([q[6], q[8]], q[9])
    x.ctrl([q[0]], q[2])
    x.ctrl([q[3]], q[5])
    x.ctrl([q[6]], q[8])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)