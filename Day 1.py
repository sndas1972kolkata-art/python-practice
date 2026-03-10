# Details
Name = input("Enter your name: ")
Age = input("Enter your age: ")
College = input("Enter your college: ")
print("Hi, I am ",Name, ".")
print("I am ", Age, "years old." )
print("I am in ", College, ".")
# Simple Calculator
n = (input("Enter a Symbol +, -, *, / : "))
a = int(input("Enter the First Number "))
b = int(input("Enter the Second Number "))
if(n == '+'):
    Sum=a+b
    print("The answer is ",Sum)
elif(n == '-'):
    Diff=a-b
    print("The answer is ",Diff)
elif(n == '*'):
    Mul=a*b
    print("The answer is ",Mul)
elif(n == '/'):
    Quo=a/b
    print("The answer is ",Quo)
else:
    print("INCORRECT SYMBOL!!!")
