# input=A5C4
# output=AAAAACCCC

s1='A5C3E3'
out=""
for x in range(len(s1)):
    if s1[x]>='A' and s1[x]<='Z':
        out=out+s1[x]*int(s1[x+1])
print(out)
        
