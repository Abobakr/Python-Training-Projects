# Read the student's degrees A, B, C
# if A>B>C or C>B>A
# median=B
# if B>A>C or C>A>B
# median=A
# if B>C>A or A>C>B
# median=c
# Print (median)
A = int(input('Enter your first NO please: '))
B = int(input('Enter your second NO please: '))
C = int(input('Enter your third NO please: '))
if A > B > C or C > B > A:
    median = B
elif B > A > C or C > A > B:
    median = A
# if B > C > A or A > C > B:
else:
    median = C

print('median =' + str(median))