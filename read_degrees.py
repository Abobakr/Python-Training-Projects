N = int(input("please enter degrees count "))
std = [0] * N
i = 0
while i < N:
    std[i] = int(input("please enter student degree "))
    i = i + 1
print("students' degrees are", std)
i=0
max=std[0]
while i<N:
	if std[i]>max:
		max=std[i]
	i=i+1
i=0
min=std[0]
while i<N:
	if std[i]<min:
		min=std[i]
	i=i+1
range=max-min
print("range is ", range )