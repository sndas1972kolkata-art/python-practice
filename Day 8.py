#Reverse String
S=input("Enter a string: ")
rev=S[::-1]
print("Reversed string: ",rev)
#First & Last Character
s=input("Enter a String: ")
if len(s)>1:
    new_s=s[-1]+s[1:-1]+s[0]
else:
    new_s=s
print("After swapping: ",new_s)
