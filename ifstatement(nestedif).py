# A SHOPPING PROGRAM
beans = 300
rice = 500
beef = 750
egg = 200
milk = 600
print("WE SELL FOOD PRODUCTS LIKE \n BEANS \n RICE \n BEEF \n EGG \n MILK only!!!!")
chioma_money = int(input("please enter the amount you have: "))
food = input("what do you want: ")
while food != "nothing" or "quit":
    if food == "beans":
        print(f"it costs {beans}NGN")
        ask = input("buying (yes or no?) ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - beans
            print(f"ping ping !!! you have {chioma_money}NGN left")
            break
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes or no) is allowed")
    elif food == "rice":
        print(f"it costs {rice}NGN")
        ask = input("buying(yes or no?)? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - rice
            print(f"ping ping!! you have {chioma_money}NGN left")
            break
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes or no) is allowed")
    elif food == "beef":
        print(f"it costs {beef}NGN")
        ask = input("buying(yes or no?)? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - beef
            print(f"ping ping!!{chioma_money}NGN left")
            break
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes or no) is allowed")
    elif food == "egg":
        print(f"it costs {egg}NGN")
        ask = input("buying(yes or no?)? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - egg
            print(f"ping ping!!{chioma_money}NGN left")
            break
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes or no) is allowed")
    elif food == "milk":
        print(f"it costs {milk}NGN")
        ask = input("buying(yes or no?)? ")
        if ask.lower() == "yes":
            chioma_money = chioma_money - milk
            print(f"ping ping!!{chioma_money}NGN left")
            break
        elif ask.lower() == "no":
            print("thanks for shopping")
            break
        else:
            print("invalid response")
            print("either (yes or no) is allowed")
    else:
        print("invalid food item entered")
        break
print("thanks for shopping with us")


#dictionary in python
#user registration 
users = {}
new_user = {}
requested_data =["first_name", "last_name", "nick_name","password", "comfirm_password"]

for data in requested_data:
    if data == "password":
        passwd = input(f"enter {data}: ")
    elif data == "comfirm_password":
        passwd2 = input(f"enter {data}: ")
    else:
        info = input(f"enter {data}: ")
        new_user.update({data:info})
else:
    if passwd == passwd2:
        new_user.update({"password":passwd})

print(new_user)