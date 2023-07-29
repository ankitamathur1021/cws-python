"""
Ask 1 mark

91-100 -> A
81-90 -> B
71-80 -> C
61-70 -> D
0-60 -> E
\-\-
5\5\/*
Invalid
"""
mark = float(input("Enter marks = "))
if mark >= 91 and mark <= 100:
    print("A")
elif mark >= 81 and mark <= 90:
    print("B")
elif mark >= 71 and mark <= 80:
 - print("C")
elif mark >= 61 and mark <= 70:
    print("D")
elif mark >= 0 and mark <= 60:
    print("E")
else:
    print("Invalid")