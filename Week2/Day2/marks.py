"""Ask 3 marks from user. Out of 100

If pass in all subjects
Then only print total and percentage

FAIL
"""
sub1=int(input("Enter marks for subject 1 :"))
sub2=int(input("Enter marks for subject 2 :"))
sub3=int(input("Enter marks for subject 3 :"))

if sub1>=33 and sub2>=33 and sub3>=33 :
    total = sub1 + sub2 +sub3
    percentage =(total/300)*100
    print(f"your result is pass and total persentage is :{percentage}")
else  :
    print("fail")
