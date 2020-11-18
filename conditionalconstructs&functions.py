num= float(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number")
    print(num, "is a positive number")
#CHAINED CONDITION
print("==================")
gen = input("Enter your gender: ")
if gen.lower() == "m":
     print("Correct guy!!!!!")
elif gen.lower()=="f":
     print("Sure Babe!!!!")
elif gen.lower()=="h":
    print("!!!!!!!")
elif gen.lower()=="t":
    print("trans")
else:    
    print("Gender Unknown") 

print("===================") 

#NESTED IF
height = 5.8
compl = "fair"
face = "round"

name = input("Enter your name: ")
if name.lower() == "zainab":
    print("Chuks has been looking for you.")
    print("Please answer the following questions for verification.")
    zHeight = float(input("How tall are you(FT): "))
    if zHeight == height:
        print("Nice, two more questions to go")
        zCompl = input("Your complextion:")
        if zCompl==compl:
            print(":), ;), ZAINAB!! long tym no see. Linkup?")
    else:
        print("Sorry,Wrong person")
else:
    print("Thank you for using my application.")                

