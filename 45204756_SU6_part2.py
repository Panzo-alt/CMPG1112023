#Panashe Tarusenga:45204756

print("Quadratic root calculator")

#Import math module
import math

#Obtain values 'a' , 'b' , 'c'
A = float(input("Enter the value of a: "))
B = float(input("Enter the value of b: "))
C = float(input("enter the value of c: "))

#Calculations
x1 = (((-1 * B) + math.sqrt((B ** 2) - 4 * A * C))/2 * A)
x2 = (((-1 * B) - math.sqrt((B ** 2) - 4 * A * C))/2 * A)

#Output
print(" Roots of given quadratic equation are: ")
print("x1:" , x1)
print("x2:" , x2)
