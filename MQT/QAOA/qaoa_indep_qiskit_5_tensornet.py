import cudaq
cudaq.set_target('tensornet')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(5)
    h(q[0])
    h(q[1])
    h(q[2])
    rx(-2.6436411784439646, q[0])
    h(q[3])
    rx(-2.6436411784439646, q[1])
    h(q[4])
    rx(-2.6436411784439646, q[2])
    rx(1.9303385045328598, q[0])
    rx(-2.6436411784439646, q[3])
    rx(1.9303385045328598, q[1])
    rx(-2.6436411784439646, q[4])
    rx(1.9303385045328598, q[2])
    rx(1.9303385045328598, q[3])
    rx(1.9303385045328598, q[4])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)