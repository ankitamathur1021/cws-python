"""Q3. Store marks of 5 subjects. Calculate their total and percentage
and properly print them."""

Hindi = int(input("Enter marks for Hindi: "))
English = int(input("Enter marks for English: "))
Science = int(input("Enter marks for Science: "))
Maths = int(input("Enter marks for Maths: "))
Physics = int(input("Enter marks for Physics: "))

Grand_Total =500
Total_Marks = Hindi + English + Science + Maths + Physics
Total_Persentage = (Total_Marks * 100)/Grand_Total
print(f"Your grand total is: {Total_Marks} out of {Grand_Total} and you got: {Total_Persentage}%")
