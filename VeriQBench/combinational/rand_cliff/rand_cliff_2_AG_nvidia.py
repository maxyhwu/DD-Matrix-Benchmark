import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(2)
    x(q[0])
    z(q[0])
    h(q[1])
    rz(-1.5707963267948966, q[1])
    h(q[1])
    h(q[0])
    rz(-1.5707963267948966, q[0])
    h(q[0])
    x.ctrl([q[1]], q[0])
    rz(-1.5707963267948966, q[0])
    swap(q[1], q[0])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)