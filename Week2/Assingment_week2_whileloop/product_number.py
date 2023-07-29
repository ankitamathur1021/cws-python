"""Calculate the product/multiplication of numbers from 1 to 10.
Example –&gt; 1 * 2 * 3 * … * 10 = ?"""

i=1
product=1
while i<=10:
    print(i,end=" * " )
    product = product * i
    i+=1
print(" = " ,product)