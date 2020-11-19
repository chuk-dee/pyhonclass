#COUNT LETTER 
def count_letter(word,letter):
    count = 0
    for alpha in word:
        if alpha == letter:
            count += 1
    return count

count = count_letter("banana","a")
print(count)

#SLICER
def slicer():
    word = "banana"
    print(word[1:4])

slicer()
print("====================================")

#started
def started(word,letter):
    if word[0] == letter:
        return True
    else:
        return False

c = started("banana","c")
print(c)

#4
def call_avg(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i
    avg = sum_num / len(num)
    return avg
print("the average is ", call_avg([1,2,3,4,5,6,7,8,9]))

#5
num = float(input("ENTER A NUMBER: "))
if num % 3 == 0 and num % 5 ==0:
    print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
    print("BUZZ")
else:
    print("INVALID NUMBER")

#6


