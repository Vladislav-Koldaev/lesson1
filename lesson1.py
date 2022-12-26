a1=input('Введите день месяц год первого \n')
a2=input()
a3=input()
print(a1, a2, a3)
b1=input('Введите день месяц год второго \n')
b2=input()
b3=input()
print(b1, b2, b3)
if a3<b3:
    print('Первый старше')
elif a3==b3:
    if a2<b2:
        print('Первый старше')
    elif a2==b2:
        if a1<b1:
            print('Первый старше')
        elif a1==b1:
            print('Они ровесники')
        else:('Второй старше')
    else:
        print('Второй старше')
else:
    print('Второй старше')
