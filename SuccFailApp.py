while 1:
    try:
        degree = int(input('Pleas input your degree '))
    except:
        print('please input valid number')

    else:
        if 60 <= degree <= 100:
            print('Successful')
            break
        elif 0 <= degree < 60:
            print('Failed')
            break
        else:
            print('Invalid')
