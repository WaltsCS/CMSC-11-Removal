
from tkinter.ttk import Separator


def sum_of_sqr (a): #First, finds the sum of squares

    sum_sqr = 0
    for i in range(1, a + 1):
        sum_sqr = sum_sqr + (i*i)
    return sum_sqr

a = 10
print(sum_of_sqr(a))

def sqr_of_sum (b): #second, finds the square of the sum

    sqr_sum = 0
    for i in range(1, b + 1):
        sqr_sum = sqr_sum + (i*i)
    return sqr_sum

b = 10**2
print(sqr_of_sum(b))

print(sqr_of_sum(b) - sum_of_sqr(a))

print()

x = int(input("Enter number of input: "))
print (x)
y = list[x-1](map(int, input("Enter the numbers: ").split()))

print("The bar graph based on the the numbers you entered:")

for i in range (x,y):
    for j in range(i):
        print('*', end="")
    print()


