x = int(input("Enter the Factorial no : "))


def fact(x):
    #num = int(input("Enter factorial no: "))
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
result = fact(x)
print ("The factorial is ", result)