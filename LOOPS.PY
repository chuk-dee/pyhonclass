#n = 2
#while n <= 10:
    #if n % 2 == 0:
        #print(n)
        #n = n+1

#A WHILE LOOP STARTS WITH WHILE FOLLOWED BY A CONDITION THEN(:) THEN ON THE NEXT LINE YOU WRITE THE BODY OF THE LOOP
#THE STATEMENT MUST BE INDENTED

#count = 5 
#while count <= 10:
    #print(count)
    #print("looping is interesting")
    #count = count + 1

#number = int(input("ENTER A NUMBER: "))
#while number in range(1,11):
    #print(number)
    #number = number + 1

#number = int(input("ENTER A NUMBER: "))
#count = 10
#while count >= 1:
    #product = number * count
    #print(number, "x", count, "=", product)
    #count = count - 1

#FOR LOOP
#for item in sequence:
#    statement(s)

#text =" alphabeth"
#for character in text:
    #print(character)

languages = ["english","french","german"]
for character in languages:
    print(character)

for count in range (1,6):
    print(count)

number = int(input("ENTER A NUMBER: "))
for count in range (1,11):
    product = number * count
    print(number,"x", count,"=", product)

number = int(input("ENTER A NUMBER: "))
for add in range (1,101):
    sum = number + add
    print(number, "+", add,"=", sum)
