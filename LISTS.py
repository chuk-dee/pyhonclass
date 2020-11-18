num = [1,2,3,4,5]
print(num[0:3])#starts from the first but doesn't print the 3rd which is four

print(num[0:])#prints everything from the beginning

print(num[1::2])#print(num[1::2]) start:stop:step/skip

print(num[-5:-1])#print from the beginning but not the last with index position -1 which is 5

print(num[:-1])#prints everything starting from the last

print(num[::-1])#print everything starting from the largest

print(num[0])#prints the first

name = ["jane","kemi","obi","musa"]
#del name[1]#deletes the specified element
#name.clear()
print(len(name))

print(name)

mixed = [1,"john",2,"ben"]

#changing values
mixed[1] = "ken"

#putting an element in a specific index position
mixed.insert(2,5)
print(mixed)
print(len(mixed))

#removing elements
mixed.remove(2)#using .remove you are removing the element not by using the index number
print(mixed)

#removing the last element
mixed.pop(0)#using .pop removes with the index number
print(mixed)
print(type(mixed))

#FUNCTIONS
mixed.append("new value")#adds the value in the string to your list
print(mixed)

name.extend(mixed)#it joins the two list together
print(name)

name = mixed.copy()#copies what in the mixed to name and prints it as name
print(name)

num2 = ["5","1","3",'mike','ada']
num2.sort()#it arranges it in order
print(num2)


