#Temperature conversion/calculator
c = float(input("Enter temperature in Celsius: "))
f=c*9/5+32 #formular to convert temperature from celcius to fahrenheit
print(f"Temperature in Fahrenheit is {f}F." )
print("====================")
print("The temperaturein in Fahrenheit is", f)

X = 7
Y = X * 2
print(Y)

count = 0
while count < 8:
    print("confirm")
    count += 4

val1 = 2
val2 = 2
print(val1 == val2)

fst_score = float(input("enter a number: "))
snd_score = float(input("enter a number: "))
if fst_score == 50 and snd_score >= 30:
    print("good one")
else:
    print("not good")


money = int(input("ENTER YOUR AMOUNT: "))
jumpMan_colour = input("ENTER A COLOUR: ")
jumpMan_price = 5000

if money > 5000:
    print("all right, you might get a shoe")
    if jumpMan_price <= 50_000:
        if jumpMan_colour == "black":
            jumpMan_price = 25_000
            if money == jumpMan_price:
                print("purchase successful")



beans = 300
rice = 500
beef = 750
egg = 200
chioma_money = 1_500

food = input("what do you want: ")
if food == "beans":
    print(f"it costs {beans}NGN")
    ask = input("buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - beans
        print(f"ping ping !!! you have {chioma_money} left")
    elif ask.lower() == "no":
        print("thanks for shopping")
    else:
        print("invalid response")
elif food == "rice":
    print(f"it costs {rice}NGN")
    ask = input("buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - rice
        print(f"ping ping!! you have {chioma_money} left")
    elif ask.lower() == "no":
        print("thanks for shopping")
    else:
        print("invalid response")
elif food == "beef":
    print(f"it costs {beef}NGN")
    ask = input("buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - beef
        print(f"ping ping!!{chioma_money} left")
    elif ask.lower() == "no":
        print("thanks for shopping")
    else:
        print("invalid response")
else:
    print(f"it costs {egg}NGN")
    ask = input("buying? ")
    if ask.lower() == "yes":
        chioma_money = chioma_money - egg
        print(f"ping ping!!{chioma_money}left")
    elif ask.lower() == "no":
        print("thanks for shopping")
    else:
        print("invalid response")

