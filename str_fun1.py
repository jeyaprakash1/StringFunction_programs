# find count a occurrence of a given substring

sen=input(" enter a string ") # python is very very easy
length=len(sen)
position=-1
count=0
word=input("enter word you want ")
while True: 
    position=sen.find(word,position+1,length)
    if position==-1:
        break
    count+=1
    print(position)
    
if count==0:
    print("given word is not present at all")
else:
    print(word,"is present",count,"times")
    
