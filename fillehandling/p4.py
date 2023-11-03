f=open('exam.txt','r')
# f.close()
f.red() # mean it gives all the line of a program 

 
v=f.readlines()  # convert list to all the  line of the file  it gives in the form of list 

print(f.tell())  # tell  the position of the curser 
print(f.seek(0))  # set the position of the curser
print(f.tell())
print(f.read())


# for i in range(len(v)):
#     print(v[i])
#     g=open('myexper.text','a')
#     g.write(v[i])