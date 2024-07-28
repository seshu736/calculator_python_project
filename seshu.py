print("1 = Addition ")
print("2 = Subtraction ")
print("3 = Multiplication ")
print("4 = Division ")

option = int(input("Enter a option:"))
result=0

if (option in [1,2,3,4]):
    num1=float(input("Enter First number:"))
    num2=float(input("Enter Second number:"))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1//num2

else:
    print("Invalid operation entered")

print("The result is {}".format(result))




