number	=	23
running	=	True
while running:
    guess=int(input('enter an interger: '))
    if guess==number:
        print('congratulations')
        running=False
    elif guess<number:
        print('lower')
    else:
        print('higer')
else:
     print('loop is over')
print('done')
