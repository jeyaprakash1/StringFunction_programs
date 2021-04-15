# merge letters fro two strings alternatively
# input :s1= tamil,s2= english
# output:teanmgilish
# Approach2
s1=input("Enter s1 ")
s2=input("Enter s2 ")

out=""
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        out=out+s1[i]
        i+=1
    if j<len(s2):
        out=out+s2[j]
        j+=1
print(out)

