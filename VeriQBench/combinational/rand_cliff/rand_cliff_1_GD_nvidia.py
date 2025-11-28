import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(1)
    s(q[0])
    h(q[0])
    z(q[0])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)