a=input('Vvedite vozrast (1;99) ')
b=a[-1]
if int(a)>11 and b=='1':
    print('мне ',a,' год')
elif int(b)>=2 and int(b)<=4:
    print('мне ', a, ' годa')
else:
    print('мне ', a, ' лет')