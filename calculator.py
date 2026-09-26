print( "                                           this is my mini project of calculator")

print("                                                   SIMPLE CALCULATOR")
while True:
    print("\n choose an operation:")
    print("1. additiom(+)")
    print("2. substraction(-)")
    print("3. multiplication(*)")
    print("4. division(/)")
    print("5. reminder(%)")
    print("6. exit:")

    choice = input("enter your choice (1-6)")

    if choice=="6":
        print(" THANK YOU FOR USING CALCULATOR")
        break
    if choice not in[ "1", "2", "3", "4", "5" ]:
        print ("INVALID CHOICE PLEASE ENTER YOUR CHOICE AGAIN")
        continue
    num1= int(input(" ENTER YOUR FIRST NUMBER:"))
    num2= int (input("ENTER YOUR SECOND NUMBER:") )  

    if choice=="1":
        result= num1 + num2
        print("result=" , result) 

    elif choice=="2":
        result= num1 - num2
        print("result=", result)

    elif choice=="3":
        result= num1 * num2
        print("result=", result)

    elif choice=="5":
        result= num1 % num2
        print("result=", result)

    elif choice=="4":
        if num2==0:
            print("ERROR , INVALID INPUT")  
        else:
             result= num1 / num2
             print("result=", result)