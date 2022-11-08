import random

file = open("DATA2.txt", "a")

list1 = []

n = input("Enter the amount of integers between 2 and 100: ")
file.write(n)
n = int(n)

i = 0
while i < n:
    num = input("Enter a positive integer: ")
    file.write("\n")
    file.write(num)
    num = int(num)
    list1.append(num)
    i = i + 1

N = input("Enter a number between 2 and 1000 (the value of the expression): ")
file.write("\n")
file.write(N)
N = int(N)
file.write("\n")

file.close()

file = open("DATA2.txt", "r")

a = 0
while a < n + 2:
    file.readline()
    a = a + 1

file.close()

expression = str(list1[0])

i = 0
j = 0
sum1 = list1[0]
while i < len(list1)*100000 - 1:
    sign = random.randint(1, 2)
    if sign == 1:
        sum1 = sum1 + list1[j + 1]
        expression = expression + " + " + str(list1[j + 1])
    elif sign == 2:
        sum1 = sum1 - list1[j + 1]
        expression = expression + " - " + str(list1[j + 1])

    i = i + 1
    j = j + 1

    if j == len(list1)-1 and sum1 == N:
        expression = expression + " = " + str(N)
        i = len(list1)*100000
    elif j == len(list1)-1 and sum1 != N:
        j = 0
        sum1 = list1[0]
        expression = str(list1[0])

print(expression)

def sumExpression(N, list1):
    expression = str(list1[0])

    i = 0
    j = 0
    sum1 = list1[0]
    while i < len(list1)*100000 - 1:
        sign = random.randint(1, 2)
        if sign == 1:
            sum1 = sum1 + list1[j + 1]
            expression = expression + " + " + str(list1[j + 1])
        elif sign == 2:
            sum1 = sum1 - list1[j + 1]
            expression = expression + " - " + str(list1[j + 1])

        i = i + 1
        j = j + 1

        if j == len(list1)-1 and sum1 == N:
            expression = expression + " = " + str(N)
            i = len(list1)*100000
        elif j == len(list1)-1 and sum1 != N:
            j = 0
            sum1 = list1[0]
            expression = str(list1[0])

    return expression, sum1

expression2 = sumExpression(N, list1)


k = 0
while k < 1000:
    if expression2[0] == expression:
        sumExpression(N, list1)
    elif expression2[0] != expression:
        print(expression2[0])
        break
    k = k + 1

expression3 = sumExpression(N, list1)

k = 0
while k < 1000:
    if expression3[0] == expression or expression3[0] == expression2[0]:
        sumExpression(N, list1)
    elif expression3[0] != expression and expression3[0] != expression2[0]:
        print(expression3[0])
        break
    k = k + 1