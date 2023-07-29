"""Q3. Write a program that calculates sum of the squares of the first
10 natural numbers (1 to 10).
Output:
The sum of the squares of the first 10 natural numbers is: 385
In the above example, the program calculates the sum of the
squares of the first 10 natural numbers (1^2 + 2^2 + 3^2 + ... + 10^2)
using a loop and outputs the result to the user. The answer to this
problem is 385."""

i=1
j=10

while i<=j:
    squre=i**(1/2)
    print(squre,end=" ")
    i=i+1
    