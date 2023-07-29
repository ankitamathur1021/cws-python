"""Ask a number from user and store it n. Write a program to find
the sum of the series 1 + 1/2 + 1/4 + 1/8 + ... + 1/2^n."""

n=int(input("Enter the number "))
num1=0
i=1
while i<=n:
    print(n ,end=" ")
    num1=num1+(1/i)
    i=i+1