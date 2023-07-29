"""2nd

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * """
for i in range(1,6):
   for j in range(5,i,-1):
    print(" ",end=" ")
   for k in range(1,2*i):
     print("*",end=" ")
   print("")  

for i in range (5,0,-1):
      i=i+1
print(" ",end=" ")
for j in range(1,(2*i)):
    print("*",end=" ")
print("")     