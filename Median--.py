A = int(input('enter A '))
B = int(input('enter B '))
C = int(input('enter C '))
if A < B:
    if A > C:
        print(f'Median is A = {A}')
    elif C < B:
        print(f'Median is C = {C}')
    else:
        print(f'Median is B = {B}')
elif B > C:
    print(f'Median is B = {B}')
elif A < C:
    print(f'Median is A  = {A}')
else:
    print(f'Median is C  = {C}')
