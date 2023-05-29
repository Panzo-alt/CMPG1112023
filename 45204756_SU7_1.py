#Panashe Tarusenga: 45204756

#Obtain data from user
age = int(input("Please enter your age: "))
ID = input("Please enter your ID status(Y/N): ")


#if statements
if ID == 'N' or ID == 'n':
    print("Invalid status")
elif age >= 18:
    print("You are eligible to buy alcohol")
else:
    print("You are not eligible to buy alcohol")
    
