"""Q6. Ask number of games played in a tournament. Ask the user
number of games won and number of games loss. Calculate
number of tie and total Points. (1 win= 4 points, 1 tie =2 points)"""

totalMatch = int(input("How many games do you played in tournament ?: "))
wonMatch = int(input("How many games you won ?: "))
lossMatch = int(input("How many games you loss ?: "))

tieMatch = totalMatch - wonMatch -lossMatch
wonMatchpoint = wonMatch*4  # 1 win = 4 point
tieMatchpoint = tieMatch*2  # 1 tie = 2 Point
totalPoint = wonMatchpoint + tieMatchpoint

print(f"Total tie match is : {tieMatch},and total earn point in tournament is :{totalPoint} ")