print("Basic Calculator (MDAS)")
print("Please choose among these operations")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("\n")
a=input("Insert the choosen operation: ")
if a=="A":
    a1=int(input("Input the first number: "))
    a2=int(input("Input the second number: "))
    print("Calculating the answer")
    s=a1+a2
    print("The Answer in these operation is: "+str(s))
elif a=="B":
    a1=int(input("Input the first number: "))
    a2=int(input("Input the second number: "))
    print("Calculating the answer")
    s=a1-a2
    print("The Answer in these operation is: "+str(s))
elif a=="C":
    a1=int(input("Input the first number: "))
    a2=int(input("Input the second number: "))
    print("Calculating the answer")
    s=a1*a2
    print("The Answer in these operation is: "+str(s))
elif a=="D":
    a1=int(input("Input the first number: "))
    a2=int(input("Input the second number: "))
    print("Calculating the answer")
    s=a1/a2
    print("The Answer in these operation is: "+str(s))
    print("Thank you for using Basic calculator (MDAS)")
else:
    print("Please Try Again. Make sure to use capital letters")
