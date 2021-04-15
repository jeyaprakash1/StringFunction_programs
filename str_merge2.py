# merge letters from two strings alternatively
# input :s1= tamil,s2= english
# output:teanmgilish
# Approach1

s1=input("Enter s1 ")
s2=input("Enter s2 ")
if len(s1)<len(s2):
    l=len(s1)
elif len(s1)>len(s2):
    l=len(s2)
output=""    
    
for i in range(l):
    output=output+s1[i]+s2[i]
    i+=1
if s1<s2:
    output=output+s2[i:]
elif s1>s2:
    output=output+s1[i:]
print(output)




