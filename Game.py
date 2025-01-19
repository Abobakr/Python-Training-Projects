name = input('Hello user. Enter your name please: ')
print('Hello ' + name)

age = int(input('Enter your age please: '))
while age <= 5:
    print('age is not valid')
    age = int(input('Enter your age please: '))

weight = int(input('Enter your weight please: '))
while weight >= 120:
    print('weight is not valid')
    weight = int(input('Enter your weight please: '))

mood_rate = float(input('Enter your mood_rate % please: '))
while mood_rate > 100:
    print('weight is not valid')
    mood_rate = float(input('Enter your mood_rate % please: '))

satus = input('Are you married (yes/no) : ')
is_married = bool(satus.upper() == 'YES')
study_hours = (weight/age)*mood_rate/100
if is_married:
    study_hours = study_hours/2
print('Your study hours is: ' + str(study_hours))