#fh = open("files.txt")

#count = 0 
#for line in fh:
    #print(line)
    #count += 1
#print(count)

#line = fh.read()
#print(line[0:12]) #slicing

#for line in fh:
    #if line.startswith("g"):
        #print(line)

#for line in fh:
    #line = line.rstrip()
    #if line.find('@gmail') == -1:
        #continue
    #print(line)

#fname = input("enter the file name: ")
fh = open("files.txt")
#count = 0
#for line in fh:
    #if line.startswith('subject.'):
        #count = count + 1
    
#print(f"there were {count} subject lines in {fh}")

file_1 = open("demo.txt","w")# w- means write mode - it wipes of everything in the file
file_1 = open("demo.txt","a")#a - append mode - it continues from where the file stopped
file_1.write("how are you")






