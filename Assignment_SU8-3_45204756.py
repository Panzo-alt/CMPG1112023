# Panashe Tarusenga- 45204756

#Greetings
name = input("Please enter your name: ")
print("\n")
print("Hello" , name , "I hope you are well.")

#User inputs
print("\n")
radius = float(input("Please enter the radius of your helix: "))
height = float(input("Please enter the height of your helix: "))
a = float(input("Please enter the a value of your ellipse: "))
b = float(input("Please enter the b value of your ellipse: "))
c = float(input("Please enter the c value of your ellipse: "))

#Calcs
import math
v_of_helix = int((math.pi) * (radius ** 2) * height)
v_of_ellipse = int((4/3) * (math.pi) * a * b * c)

#output
print("\n")
print("r = ", radius ,"cm" , " h = " , height ,"cm" , "\t" , "volume= ", v_of_helix , "cm3" )
print("a = ", a,"cm" , "b = ", b,"cm" , "c = ", c,"cm" , "\t" , "volume= ", v_of_ellipse , "cm3")

#Choice to end program
print("\n")
while True:
    choice = input("Would you like to end the program (1=yes): ")
    yes = 1
    if choice != 1:
        print("You are amazing" , name)
        break
    else:
        break
    
    
