import random
a = random.randrange(0,100)
b = int(input('Guess number from 1 to 100: '))

if a>b:
    print('My number is greater than,', b)
elif a<b:
    print('My number is smaller than,', b)
elif a==b:
    print('That`s right, my number is ', a)

b1 = int(input('Guess number from 1 to 100: '))

if a>b1:
    print('My number is greater than,', b1)
elif a<b1:
    print('My number is smaller than,', b1)
elif a==b1:
    print('That`s right, my number is ', a)

b2 = int(input('Guess number from 1 to 100: '))

if a>b2:
    print('My number is greater than,', b2)
elif a<b2:
    print('My number is smaller than,', b2)
elif a==b2:
    print('That`s right, my number is ', a)

b3 = int(input('Guess number from 1 to 100: '))

if a>b3:
    print('My number is greater than,', b3)
elif a<b3:
    print('My number is smaller than,', b3)
elif a==b3:
    print('That`s right, my number is ', a)    

b4 = int(input('Guess number from 1 to 100: '))

if a>b4:
    print('My number is greater than,', b4)
elif a<b4:
    print('My number is smaller than,', b4)
elif a==b4:
    print('That`s right, my number is ', a)

if b!=a and b1!=a and b2!=a and b3!=a and b4!=a:
    print('Sorry, you lost. My number was,', a)