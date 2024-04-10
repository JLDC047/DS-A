
n = 7


def number(number):
    sum = 0
    for i in range(1,number+1):
        sum += i
    print(sum)

number(n)

def sum(number):
    if number == 1:
        return number
    else:
        return number + sum(number-1)

print(sum(n))

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)

print(factorial(int(n)))

def fibonacci(amount):
    if amount == 1 or amount == 0:
        return amount
    else:
        return fibonacci(amount-1) + fibonacci(amount-2)

print(fibonacci(n))

