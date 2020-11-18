#def staff_location():
    #name = input("Enter user name: ")
    #sex = input("Enter your sex: ")
    #age = int(input("Enter your age: "))
    #Marital_status = input("marital status: ")

    #if sex.lower() == "female" or "f":
        #print("You are allowed to work only in urban areas")
    #elif (sex.lower() == "male" or "m") and (age in range(20, 40)):
        #print("You can work anywhere")
    #elif (sex.lower() == "male" or "m") and (age in range(40, 60)):
        #print("You are allowed to work only in urban areas")
    #else:
        #print("ERROR")

# staff_location()

def myfunction():
    print("hello world")


def greet_user(name):
    print(f"hello{name}")

greet_user(" jesse ")

def reminder(num):
    if num % 2 == 0:
        print("THE NUMBER IS EVEN")
    else:
        print("THE NUMBER IS ODD")

reminder(10)

def largest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the largest")
    elif num2 > num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the greatest")

largest(57,7,1)

def add(a,b):
    return a + b
sum = add(3,4)
print(sum)

def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False
value = is_even(9)
print(value)