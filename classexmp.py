num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("BUZZ")
elif num % 5 == 0:
    print("FIZZ")
else:
    print(f"{num}, is not a multiple of 3 or 5")    

print("============================================")