# Given a list A of numbers, you have to print those numbers which are not multiples of 3.
#
# Input Format:
#
# The first line contains the numbers of list A separated by a space.
#
# Output Format:
#
# Print the numbers in a single line separated by a space which are not multiples of 3.
#
# Example:
#
# Input:
#
# 1 2 3 4 5 6 5
#
# Output:
#
# 1 2 4 5 5


a = [int(x) for x in input().split()]
for i in range(len(a)):
    if ((a[i] % 3) != 0):
        print(a[i], end=" ")


# or


a = [int(x) for x in input().split()]

b = []

for i in a:
    if(i % 3 != 0):
        b.append(i)

for i in range(len(b)):
    if(i == len(b)-1):
        print(b[i], end="")
    else:
        print(b[i], end=" ")
