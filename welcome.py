name = input("enter your name : ")
print("hello "+name)
play_study_answer = input("what do you want to do? Play or Study?")
if str.upper(play_study_answer) == "PLAY":
    print("ok lets play")
    ball_answer = input("do you have a ball?yes or no?")
    if str.upper(ball_answer) == "yes":
        print("play football")
    elif str.lower(ball_answer) == "no":
        print("other question...")
        friends_answer = input("are you with friends?yes or no?")
        if str.lower( friends_answer ) == "yes":
            print("play ebelemece")
        elif str.lower( friends_answer )=="no":
            print("no idea")
        else:
            print("bad answer")
    else:
        print("bad answer")
elif str.lower(play_study_answer) == "study":
    print("ok lets study")
    age = int(input('Enter your age please: '))
    while age <= 5:
        print('age is not valid')
        age = int(input('Enter other age larger then 5 please: '))

    weight = int(input('Enter your weight please: '))
    while weight >= 120:
        print('weight is not valid')
        weight = int(input('Enter another weight smaller then 120 please: '))

    mood_rate = float(input('Enter your mood rate % please: '))
    while mood_rate > 100:
        print('mood rate  is not valid')
        mood_rate = float(input('Enter your mood rate < 100% please: '))

    satus = input('Are you married (yes/no) : ')
    is_married = bool(satus.upper() == 'YES')
    study_hours = (weight / age) * mood_rate / 100
    if is_married:
        study_hours = study_hours / 2
    print('Your study hours is: ' + str(study_hours))
else:
    print("bad answer")
