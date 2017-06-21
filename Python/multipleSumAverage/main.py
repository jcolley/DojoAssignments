"""
Multiple, Sum, Average Assignment
"""

for num in range(0, 1001):
    if num%2 == 0:
        print num

print "\n============================\n"

for num in range(5, 1000001):
    if num%5 == 0:
        print num

print "\n============================\n"

a = [1, 2, 5, 10, 255, 3]
b = 0
for i in a:
    b += i

print b

print "\n============================\n"

c = b / len(a)
print c