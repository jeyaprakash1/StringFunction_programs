# find how many times particular word is present in string without using find function

sen=input("enter a sentence ")
word=input("enter a word you want ")
count=0
position=0
for x in sen:
    if x==word:
        print(word,"is present at:",position)
        count+=1
    position+=1
else:
    print(count)
    
