# Panashe Tarusenga: 45204756

#Obtain data form user

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
ope = input("Enter the operator(+ - * /):  ")

#if statements
if second == 0 and ope == '/':
    print("Error: division by zero")
elif ope != '+' and ope != '-' and ope != '*' and ope != '/':
    print("Error: invalid operator")
elif ope == '+':
    print("The result is: " , first + second)
elif ope == '-':
    print("The result is: " , first - second)
elif ope == '*':
    print("The result is: " , first * second)
else:
    print("The result is: " , first / second)

                
    
