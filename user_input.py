# input from user
a = input("Enter value: ")
print(a)

# addition of two number
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
addition = a + b
print('sum of a and b is', addition)

# addition of two number
value1 = int(input("Enter value1: "))
value2 = int(input("Enter value2: "))
addition = a + b
print('sum of {} and {} is {}'.format(value1,value2,addition))

# print name in reverse order
first_name = input('Enter the first name:')
last_name = input('Enter the last name:')
print('Welcome',last_name,'',first_name)


# print numbaer in specified range
lower = int(input('Enter the value: '))
upper = int(input('Enter the value: '))
for num in range(lower, upper + 1):
    print(num)


# even number in given range
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
for i in range(value1,value2+1):
    if i % 2 == 0:
        print(i,'is even number')

# odd number in given range
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
for i in range(value1,value2+1):
    if i % 2 != 0:
        print(i,'is odd number')

# prime number in given range
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
for prime in range(value1,value2+1):
    if prime > 1:
        for number in range(2,prime):
            if prime % number == 0:
                break
        else:
            print(prime)
    else:
        print('Enter positive value')


# factorial of given value
value = int(input('Enter the value:'))
fact = 1
for i in range(1,value+1):
    fact *= i
print('The factorial of {} is {}'.format(value,fact))