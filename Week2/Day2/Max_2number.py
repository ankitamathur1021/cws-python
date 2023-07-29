"""ask two number from user
print which is greatest
if-elif-else
indantation error means 4 space
"""
n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))
if n1 > n2 :
    print(f"{n1} is greater")
elif n2 >n1 :
    print(f"{n2} is greater")
else:
    print("Both are equal")