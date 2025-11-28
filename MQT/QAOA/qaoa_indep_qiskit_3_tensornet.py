import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(3)
    h(q[0])
    h(q[1])
    h(q[2])
    rx(-6.860310317223841, q[0])
    rx(-6.860310317223841, q[1])
    rx(-6.860310317223841, q[2])
    rx(8.165927224507852, q[0])
    rx(8.165927224507852, q[1])
    rx(8.165927224507852, q[2])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)