#def my_function(name,age):
    #print(name + "is" + age + "yrs old")
#first_name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("you are "+ first_name+ " and you are "+age+ " years old")

def greet(name):
    print(f"hello {name} hw do you do?")
    return
    print("======")

greet("jack")

def add_number(n1,n2):
    result = n1 + n2
    return result
result = add_number(2,4)
print(f"the sum is {result}")

#function to find average mark
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks/total_subjects
    return average_marks

# calculate the grade and return it
def compute_

marks=[55,64,75,80,65]
average_marks = find_average_marks(marks)
print("Your average mark is:", average_marks)


