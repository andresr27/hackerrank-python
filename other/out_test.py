#!/usr/bin/python3
class C:
    danger = 2

c1 = C()
c2 = C()

print(c1.danger) #2

c1.danger = 3

print(c1.danger) #3
print(c2.danger) #2


del c1.danger
print(c1.danger) #2

C.danger = 3
print(c2.danger) #3
print(c1.danger) #3
