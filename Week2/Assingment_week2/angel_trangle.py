"""Q3. Write a program to check the triangle is isosceles, scalene,
equilateral and right angled by entering angles of triangle."""

side1=int(input("Enter trangle side1 : "))
side2=int(input("Enter trangle side2 : "))
side3=int(input("Enter trangle side3 : "))
if side1==side2 and side2==side3:
    print("Trangle is euilateral")
elif side1==side2 or side2==side3 or side3==side1:
    print("Trangle is scalane")
else:
    print("Trangle is isosceles")