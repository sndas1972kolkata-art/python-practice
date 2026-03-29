#Countdown
n=int(input("Enter a number "))
for i in range(n,-1,-1):
    print(i)
#Sum until 0 entered
sum=0
a=int(input("Enter a number "))
while(a!=0):
 sum=sum+a
 a=int(input("Enter a number "))
print(sum)
#Guess number logic
secret=6
guess=int(input("Enter your guess number "))
while guess != secret :
 if(secret>guess):
   print("TOO LOW")
 else:
   print("TOO HIGH")
 guess=int(input("Enter your guess number "))
print("CORRECT")
