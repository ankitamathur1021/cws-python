"""20
1 2 4 5 10 20"""

num=int(input("enter a number= "))
for i in range(1,num+1):
    if num%i==0:
      print(i,end=" ")