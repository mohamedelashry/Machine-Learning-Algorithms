from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = a>10
c = a<15

print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
