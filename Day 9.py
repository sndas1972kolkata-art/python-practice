#Count Vowels
def count_vowels(s):
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
s=input("Enter a string : ")
print(count_vowels(s))
#Palindrome check
def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
s=input("Enter a string : ")
print(is_palindrome(s))
