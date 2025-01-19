student = [244657384756, 839565485044, 2947593047, 6685903046204, 749563446289734]
N = len(student)
max = student[0]
for i in range(N):
    if max < student[i]:
        max = student[i]
print("max = " + str(max))
