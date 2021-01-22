# Edited for debugging by Robert Tate on 1/22/21
# 
# Gets current time and wait time from user and prints the time
# when the wait will be completed

currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt) % 24
print(str(finalTimeInt))
