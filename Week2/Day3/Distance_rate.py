
"""
Distance Rate Calculator 

Ask distance from user (km)

Base Price upto 5km - 100Rs
5-10km -> 50rs/km
10-15km -> 40rs/km
15-20km -> 30rs/km
20 above -> 15rs/km

3km -> 100Rs

7km -> 5+2 -> 100+100 -> 200
10km -> 5+5 -> 100+250 -> 350
13km -> 5+5+3 -> 100+250+120
18km -> 5+5+5+3 -> 100+250+200+90
23km -> 5+5+5+5+3 -> 100+250+200+150+45
43km -> 5+5+5+5+23 -> 100+250+200+150+(15*23)
"""

distance = int(input("Enter distance travelled = "))
if distance <= 5 and distance > 0:
    total = 100
elif distance >= 6 and distance <= 10:
    total = 100 + ((distance - 5) * 50)
elif distance >= 11 and distance <= 15:
    total = 100 + (5 * 50) + ((distance - 10) * 40)
elif distance >= 16 and distance <= 20:
    total = 100 + (5 * 50) + (5 * 40) + ((distance - 15) * 30)
else:
    total = 100 + (5 * 50) + (5 * 40) + (5 * 30) + ((distance - 20) * 15)

print(f"Total = {total}")