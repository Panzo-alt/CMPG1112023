#Panashe Tarusenga: 45204756

#import math
import math

#Obtain data from user
name = input("Please enter your name: ")
radius = float(input("Please enter the radius: "))
height = float(input("Please enter the height: "))

#Calculations
uarea = (math.pi * radius * (radius + math.sqrt((height ** 2) +(radius ** 2))))
udia = (math.sqrt((radius ** 2) + (height ** 2)))
uvol = ((math.pi * (radius ** 2) * height) / 3)

#round values
A = round(uarea , 4)
D = round(udia , 3)
V = round(uvol , 2)

#Output
print("Area of the cone is" , A , "square cm")
print("Diagonal of the cone is" , D , "cm")
print("Volume of the cone is" , V , "cm")

print("Dimensions are: ")
print("radius = " , radius , "cm                         ","height = " , height , "cm")
              
      
      
              
                                  
