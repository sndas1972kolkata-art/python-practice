#Grade Calculator
per=float(input("Enter the percentage "))
if(90<=per<=100):
    print("Grade=A")
elif(70<=per<=89):
    print("Grade=B")
elif(40<=per<=69):
    print("Grade=C")
elif(per<=40):
    print("Grade=F") 
else:
    print("Wrong Percentage is Given")
#Leap Year Check
year=int(input("Enter the Year "))
if(year%4==0):
    print("Leap Year")
else:
    print("Not A Leap Year")
#Simple Menu Program
while True:
    print("\nMenu")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Exit")

    choice=int(input("Enter your choice: "))
    
    if choice==1:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print("Sum = ",a+b)

    elif choice==2:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        print("Diff = ",a-b)
    elif choice==3:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice! Try Again.")
