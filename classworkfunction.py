#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask a user for their salary and year of service and display their net salary using function
def bonus_salary():
    name = input("Enter username: ")
    print("Hello ",name)
    salary = float(input("Enter salary:"))
    print("Your salary is: ""$",salary,)
    year_of_service = float(input("Enter year of service: "))
    print("You have served for " ,year_of_service, " Years ")
    b = 5/100*salary
    if year_of_service > 5:
        print("Your Bonus is: ""$",5/100*salary,)
        print("Your net salary is: ""$",b + salary,)
    else:
        print("you are not eligible for the bonus") 

bonus_salary()

word = "apple"
for letter in word:
    print(word.index(letter))
