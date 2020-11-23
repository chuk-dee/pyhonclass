#x=7
#y=7
#if x >= y:
    #print("x is equal to y")
#else:
    #print("x is not greater than or equal to y")

x=7
y=8
z=10
k=15
if x == y:
    print(x)
elif y > z:
    print(y)
elif k > z:
    print(k)
else:
    print(z)

john_age = 81
wick_age = 111
paul_age = 111
if john_age > wick_age:
    print("john is older")
elif john_age == wick_age and paul_age == wick_age:
    print("same")
else:
    print("wick is older")

    print(x)
print("\tLogin")
uname = input("Username: ")
passwd = input("Password: ")
if uname.lower()=="jerry" and passwd =="1234qwer":
    print("Login Successfull")
else:
    print("Invalid Username or Password")



val1 = 2
val2 = 2
print(val1 == val2)

fst_score = float(input("enter a number: "))
snd_score = float(input("enter a number: "))
if fst_score == 50 and snd_score >= 30:
    print("good one")
else:
    print("not good")

# A SHOPPING PROGRAM
beans = 300
rice = 500
beef = 750
egg = 200
chioma_money = int(input("please enter the amount you have: "))
food = input("what do you want: ")
while food  != "nothing":
    if food == "beans":
        print(f"it costs {beans}NGN")
        ask = input("buying? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - beans
            print(f"ping ping !!! you have {chioma_money} left")
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes\no) is allowed")
    elif food == "rice":
        print(f"it costs {rice}NGN")
        ask = input("buying? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - rice
            print(f"ping ping!! you have {chioma_money} left")
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes\no) is allowed")
    elif food == "beef":
        print(f"it costs {beef}NGN")
        ask = input("buying? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - beef
            print(f"ping ping!!{chioma_money} left")
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes\no) is allowed")
    elif food == "egg":
        print(f"it costs {egg}NGN")
        ask = input("buying? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - egg
            print(f"ping ping!!{chioma_money}left")
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
    else:
        print("invalid food item entered")
        break
print("thanks for shopping with us")
