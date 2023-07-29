"""Q1. Print the following series using any loop:
a. 10 20 30 40 … 200
b. 1 10 100 1000 10000 … 100000000
c. 1 11 111 1111 11111 … 1111111111
d. 1 3 6 8 11 13 16 … 28
e. 1 2 4 8 16 32 64…2048"""

#Series (a)
print("Output of Question a:")
i=10
j=200
while i<=j:
    print(i,end=" ")
    i=i+10

#Series (b)
print("\n\nOutput of Question b:")
a=1
b=100000000
while a<=b:
    print(a,end=" ")
    a=a*10

# #Series (c)
print("\n\nOutput of Question c:")
n=10
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
i=i+1

#Series (d)
# print("\n\nOutput of Question d:")
# c=1
# d=28
# lastN=2
# while c<=d:
#     if c%2!=28 or c%3!=28:
#      print(c,end=" ")
#     c=c%2


    
