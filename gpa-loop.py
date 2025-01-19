std_old = [12, 20, 30, 36, 77, 10, 99, 3, 7, 100, 50, 75, 97,45,23,12,15, ]
N = len(std_old)
std_new=[0]*N
print(std_new)
i=0
while i<N:
    std_new[i]=std_old[i]/25
    i=i+1
print(std_new)