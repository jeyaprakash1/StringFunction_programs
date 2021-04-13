# Merging letters from two strings alternatively 

s1='pto'
s2='yhn'
i=0
output=''
while i<len(s1):
    output=output+s1[i]
    output=output+s2[i]
    i+=1
print(output)
