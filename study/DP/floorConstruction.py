N = 3 

d = [0] * 100

d[1] = 1
d[2] = 3
for i in range(3,N+1):
    d[i] = (d[i-1] +d[i-2]*2)%796796

print(d[N])
print(d)