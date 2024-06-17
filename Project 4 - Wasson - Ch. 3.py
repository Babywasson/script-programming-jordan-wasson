print("This code will calcuate the distance traveled by a ball depending on how many bounces happens.")
height = int(input("Input the height the ball is to be dropped from: "))
bounces = int(input("Input how many times you will allow the ball to bounce: "))
bounces = bounces - 1
distanceTraveled = height
for eachPass in range(bounces):
    height = height * .6
    distanceTraveled = distanceTraveled + height * 2
finalBounce = height * .6
distanceTraveled = finalBounce + distanceTraveled
print("The distance traveled by the bouncing ball is: ", distanceTraveled, "ft.")
