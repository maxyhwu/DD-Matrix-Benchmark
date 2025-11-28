import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(4)
    h(q[0])
    h(q[1])
    h(q[2])
    rx(8.63937561261258, q[0])
    h(q[3])
    rx(8.63937561261258, q[1])
    rx(8.63937561261258, q[2])
    rx(4.712387043046583, q[0])
    rx(8.63937561261258, q[3])
    rx(4.712387043046583, q[1])
    rx(4.712387043046583, q[2])
    rx(4.712387043046583, q[3])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)