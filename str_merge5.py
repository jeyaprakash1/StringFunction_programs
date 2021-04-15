# input = A5B6C7
# output= ABC567
# Approach 2

s1='A5B6C7'
out1=""
out2=""  
for letter in s1:
    if letter.isalpha():
        out1=out1+letter
    else:
        out2=out2+letter
out=out1+out2
print(out)
