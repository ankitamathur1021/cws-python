"""Q2. Write a program to input electricity unit charges and calculate
total electricity bill according to the given condition:
 For first 50 units Rs. 0.50/unit
 For next 100 units Rs. 0.75/unit
 For next 100 units Rs. 1.20/unit
 For unit above 250 Rs. 1.50/unit
 An additional surcharge of 20% is added to the bill"""

unit = float(input("Enter total unit : "))
if unit>=0 and unit<=50:
    total =0.50 * unit
elif unit>=51 and unit<=100:
    total = unit*0.50 * ((unit-50)*0.75)
elif unit>=101 and unit <=200:
    total = 0.50 * (50*0.75)+ ((unit-100)*1.20) * unit
else:
    total = 0.50 * (50*0.75) + (100*1.20) +((unit-200)*1.50) *unit
    
totalbill=((total*20)/100)+total
print(f"your total electricity bill is : {totalbill}")
