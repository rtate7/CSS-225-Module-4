# Edited for debugging by Robert Tate on 1/22/21
# 
# Gets current time and wait time from user and prints the time
# when the wait will be completed

str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time) % 24
print(time_when_alarm_go_off)
