# ETGG 1801
# Donald Stapleton
# Lab01 Hello World
# 09/05/2020
import math
firstName = 'Donald'
lastName = 'Stapleton'
opposite = 0.5
adjacent = 7
print('Lab01 created by:', firstName, lastName)
print(firstName, end=' ')
print(lastName)
hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)
print('The hypotenuse length is', hypotenuse, 'if the other sides are ', opposite, ' and ', adjacent)
print('(Press Enter to Learn Steps)')
input()
print('First, find the sum of 0.5 squared and 7 squared!')
print('(Press Enter)')
input()
print(opposite ** 2 + adjacent ** 2)
print('Now find the square root of that result!')
print('(Press Enter)')
input()
print('And you get', hypotenuse)
print('''
        THANKS
      PYTHAGORAS!
''')
print('Goodbye!')
input()
