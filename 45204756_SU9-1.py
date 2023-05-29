#Panashe Tarusenga - 45204756
#mark calculator

#User inputs
name = input("Please enter your name: ")
test1 = float(input("Please enter your test 1 mark out of 50: "))
test2 = float(input("Please enter your test 2 mark out of 50: "))
exam = float(input("Please enter your exam mark: "))
print("\n")

#Calcs
mark = ((test1/50) * 25) + ((test2/50) * 25) + ((exam/100) * 50)

#Output
if mark < 50:
    print(name , "you have failed with" , mark , "%")
elif mark <= 75:
    print(name , "you have have passed with" , mark , "%")
else:
    print(name , "you have acheived a distinction of" , mark , "%")
print("\n")

#While loop
while True:
    cont = int(input("Would you like to calculate your friend's mark 1(no) or 0(yes): "))
    if cont == 1:
        break
    #User inputs
    name = input("Please enter your name: ")
    test1 = float(input("Please enter your test 1 mark out of 50: "))
    test2 = float(input("Please enter your test 2 mark out of 50: "))
    exam = float(input("Please enter your exam mark: "))
    print("\n")

    #Calcs
    mark = ((test1/50) * 25) + ((test2/50) * 25) + ((exam/100) * 50)

    #Output
    if mark < 50:
        print(name , "you have failed with" , mark , "%")
    elif mark <= 75:
        print(name , "you have have passed with" , mark , "%")
    else:
        print(name , "you have acheived a distinction of" , mark , "%")
    print("\n")
