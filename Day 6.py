#Print 1-50
for i in range(1,51):
    print(i,end=" ")
#Sum of numbers
n=int(input("\nEnter a number "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum = ",sum)
#Multiplication Table
num=int(input("Enter a number "))
print("Multiplicatin Table of ",num)
for i in range(1,11):
    print(num,"x",i,"=",num*i)
