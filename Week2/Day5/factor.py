"""enter a number =15
1 3 5"""

num = int(input("Enter a number = "))
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count ==2:
   print("its a prime number")
else:
   print("its not a prime number")
