A = int(input('enter A '))
B = int(input('enter B '))
C = int(input('enter C '))

if C <= A <= B or B <= A <= C:
    print(f'Median is A = {A}')
elif C <= B <= A or A <= B <= C:
    print(f'Median is B = {B}')
else:  # elif B <= C <= A or A <= C <= B:
    print(f'Median is C = {C}')


