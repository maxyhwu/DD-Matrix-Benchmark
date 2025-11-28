import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(1)
    x(q[0])
    rz(-1.5707963267948966, q[0])
    h(q[0])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)