A=int(input('Enter your first NO please: '))
B=int(input('Enter your second NO please: '))
C=int(input('Enter your third NO please: '))
if A<B:
    min = A
else:
    min=B
if C<min:
    min=C
print('min =' + str (min))

