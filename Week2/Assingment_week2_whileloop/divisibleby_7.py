"""Q2. Ask start and end number from user. Print all the numbers
divisible by 5 or divisible by 7."""
start = int(input("Enter a Number : "))
end = int(input("Enter a Number : "))
i=start
while i<=end:
  
  if i%5==0 or i%7==0:
    print(i , end=" ")
  i=i+1

