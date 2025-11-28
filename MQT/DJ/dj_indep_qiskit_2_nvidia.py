import cudaq
cudaq.set_target('nvidia')
@cudaq.kernel
def circuit():
    q = cudaq.qvector(2)
    u3(1.5707963267948966,0,0, q[0])
    u3(1.5707963267948966,-3.141592653589793,-3.141592653589793, q[1])
    x.ctrl([q[0]], q[1])
    u3(1.5707963267948966,-3.141592653589793,-3.141592653589793, q[0])

counts = cudaq.sample(circuit, shots_count=1024)
print(counts)