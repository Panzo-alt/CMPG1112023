#Panashe Tarusenga: 45204756

#Obtain data from user

base = float(input("Enter the base: "))
exp = float(input("Enter the exponent: "))

#if statements
if exp < 0:
    print("Error: exponent cannot be negative")
elif exp == 0 and base == 0:
    print("Error:indeterminate form")
elif  not base == 0:
    print(base , "to the power of" , exp , "is:" , base ** exp)    
else:
    print(base , "to the power of" , exp , "is:" , base ** exp)
