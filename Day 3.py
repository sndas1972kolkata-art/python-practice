# Even/Odd
a = int(input("Enter a number: "))
if(a%2==0):
    print("Even")
else:
    print("Odd")
# Square & Cube
b = int(input("Enter a number : "))

square = b ** 2
cube = b ** 3
print("Square =", square)
print("Cube =", cube)
# Temperature Converter
print("Temperature Converter")
print("1. Celsius to Fahrenhite")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Enter your choice (1-4):")
temp = float(input("Enter temperature value: "))

if choice == "1":
    result = (temp*9/5) + 32
    print("Temperature in Fahrenhite =",result)
elif choice == "2":
    result = (temp-32) * 5/9
    print("Temperature in Celcius =",result)
elif choice == "3":
    result = temp + 273.15
    print("Temperature in Kelvin =",result)
elif choice == "4":
    result = temp - 273.15
    print("Temperature in Celcius =",result)
else:
    print("Invalid choice")
