num = [2, 3, 4, 5, 2]
N = len(num)
prod = 1
i = 0
while i < N:
    prod = prod * num[i]
    i = i + 1
print("prod = " + str(prod))