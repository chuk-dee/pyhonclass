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