#Using switch case in python

print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
a=int(input())
b=int(input())
choice=int(input('Enter Choice:'))
operation={
        1:a+b,
        2:a-b,
        3:a*b,
        4:a/b
    }
if choice in operation:
    print(operation[choice])
else:
    print('Wrong choice')


