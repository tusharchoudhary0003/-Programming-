#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#Input Format:
#The first line of the input contains a statement.

#Output Format:
#Print the number of upper case and lower case respectively separated by a space.

#Example:

#Input:
#Hello world!

#Output:
#1 9
#Sample Test Cases
#Input	Output


s = input()
u, l = 0, 0
for i in s:
    if(i.islower()):
        l += 1
    elif(i.isupper()):
        u += 1
print(u, l, end='')


s = input()
d = {"UPPER CASE": 0, "LOWER CASE": 0}
for c in s:
    if c.isupper():
        d["UPPER CASE"] += 1
    elif c.islower():
        d["LOWER CASE"] += 1
    else:
        pass
print(d['UPPER CASE'], d['LOWER CASE'])
