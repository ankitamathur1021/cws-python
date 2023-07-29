"""Write a program to print all the numbers which are divisible by
2 and 3 but not 8, from 1 to 100."""

i=1
j=100
while i<=j:
    if i%2==0 and i%3==0 and i%8!=0:
        print(i,end=" ")    
    i=i+1