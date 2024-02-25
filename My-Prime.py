while True:
    txt1 = []
    txt2 = []
    num = int(input("Number: "))
    for i in range(2, num):
        if num % i == 0:
            txt1.append(i)
    total = sum(txt1)
    if num == 1:
        print('not prime')
    elif total < 1:
        print('prime')
    else:
        print('not prime')
        