"""Write a program that takes two numbers as input, `units` and
`rate`. Calculate the cost of the light bill as `units` multiplied by
`rate`. Add 12% tax to the cost of the light bill. If the total cost of the
light bill is greater than 100 and it is a multiple of 5, print "The cost
of your light bill is ${total_cost}. There is a free gift card to your
favorite store.";. Otherwise, print "The cost of your light bill is
${total_cost}.".   """

unit = int(input("Enter total unit : "))
rate = int(input("Enter total rate : "))
cost = unit * rate
gst = (cost * 12) / 100
total_cost = cost + gst
if total_cost >= 100 and total_cost % 5 == 0:
    print(f"\"The cost of your light bill is ${total_cost}.There is a free gift card to your favorite store.\"")
else:
    print(f"\"The cost of your light bill is ${total_cost}.\"")