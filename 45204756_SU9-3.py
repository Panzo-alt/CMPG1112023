#Panashe Tarusenga - 45204756

#User inputs
name = input("Please enter your name: ")
fund = input("Please input your medical aid/fund: ")
num = input("Please input your medical aid number: ")
print("\n")

#Output
print(name , "with" , fund ,"-",num)

#While loop

while True:
    cont = int(input("Would you like to continue 1(no) or 0(yes): "))
    if cont == 1:
        break
    name = input("Please enter your name: ")
    fund = input("Please input your medical aid/fund: ")
    num = input("Please input your medical aid number: ")
    print("\n")
    
    
