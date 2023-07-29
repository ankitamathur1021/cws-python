"""Q3. Ask start and end number from user. Print the sum of all the
numbers divisible by 4."""

start = int(input("Enter a Number : "))
end = int(input("Enter a Number : "))
i=start
sum=0
while i<=end:
    if i%4==0:
     print(i,end=" ")
     sum = i + sum
    i+=1
print("\nSum of all divisible no of 4: ", sum)