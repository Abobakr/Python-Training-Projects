A=int(input('Enter your first NO please: '))
B=int(input('Enter your second NO please: '))
C=int(input('Enter your third NO please: '))
if A>B:
    max = A
else:
    max=B
if C>max:
    max=C
print('max =' +str (max))