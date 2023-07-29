"""Q5. Print the multiplication table of a number entered by User.
Example:
Enter a number = 8
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
…..
8 X 10 = 80"""

num = int(input("Enter a Number : "))
count=1
while count<=10:
    print(num ," X ",count," =",num*count)
    count=count+1
