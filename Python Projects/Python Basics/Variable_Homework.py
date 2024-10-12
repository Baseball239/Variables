
x=5
b=4
print(x)
print(b)
print("1 addition(+)")
print("2 subtraction(-)")
print("3 multiplication(*)")
print("4 division (/)")

# Taking user input
user =int( input("Please select option from (1-4)"))
if user == 1:
    z = x + b
    print("The result of addition is ", z)
elif user==2:
    z = x - b
    print("The result of subtraction is",z)
elif user==3:
    z = x * b
    print("The result of multiplication is",z)
elif user==4:
    z = x / b
    print("The result of division is",z)





