# Python program to calculate the missing numerator or denominator
#  2 / 4 = x / 8

n1 = int(input('Enter the first numerator '))
d1 = int(input('Enter the first denominator '))
print('You just enter a "0" for the x ')
n2 = int(input('Enter the second numerator '))
d2 = int(input('Enter the second denominator '))

if n2 == 0:
    answer = d2 * n1 / d1
    print('x = ', answer)

if d2 == 0:
    answer = d1 * n2 / n1
    print('x = ', answer)