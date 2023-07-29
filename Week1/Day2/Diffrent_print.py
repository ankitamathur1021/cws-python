"""Diffrent way to print veriable
int(%d) ,float(%f),string(%s),bool """
# My name is Ankita
# my age is 18
Name = "Ankita"
Hname = "Chitransh"
age=40
hage = 33
gender="female"

# Method 1
# print("My name is",Name)
# print("My age is",age)
print("my name is",Name and "my age is",age)

# Method 2 (f string)
# print(f"My name is{Name} and my age is{age}"
print(f"{Name}-{age}")
# Method 3
print("My Name is %s & My Husband name is %s & My age is %d & My Husband age is %d" %(Name, Hname, age, hage))
# print("My name is %s and my age is %d"(Name,age))
