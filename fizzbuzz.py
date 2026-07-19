print("Welcome to FizzBuzz game!")
ans = int(input("How many number do you want to play? "))
number = []
for numbers in range(1,ans+1):
    number.append(numbers)
for digit in number:
    if digit%5==0 and digit%7==0:
        print("FizzBuzz")
        continue
    elif digit%5==0:
        print("Fizz")
    elif digit%7==0:
        print("Buzz")
    else:
        print(digit)
print("Thankyou for using our program")
