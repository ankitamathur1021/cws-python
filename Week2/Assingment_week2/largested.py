"""Q6. Compare three numbers and find the largest one among
them."""
num1=int(input("Enter a Number One : "))
num2=int(input("Enter a Number Two : "))
num3=int(input("Enter a Number Three : "))
if num1>=num2 and num1>=num3:
    print(num1,"is largest")
elif num2>=num1 and num2>=num3:
    print(num2,"is largest")
else:
    print(num3,"is largest")