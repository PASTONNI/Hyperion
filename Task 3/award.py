# pseudocode
# This is the code to calculate givcen to an individual based on a triathlon event
# the qualifying time for awards is 100 minutes 
# Create an input which will be saved in the variable to save the time in minutes for the 3 events
# add the sum of the time of the three events in minutes to get TOTAL TIME
# using conditionals i.e "if-else" to check if the meet the criteria for award or not
# print the award based on the qualifying criteria

# ************CODE*************
# This section accept the time for the individual event in minutes, appends it to a list and calculates the sum.
time = []
swimming_event = int(input("Please enter the time in minutes it takes the user to complete the swimming event "))
time.append(swimming_event)
cycling_event = int(input("Please enter the time in minutes it takes the user to complete the cycling event "))
time.append(cycling_event)
running_event = int(input("Please enter the time in minutes it takes the user to complete the running event "))
time.append(running_event)
Total_time = sum(time)


# This section checks the conditionals of the total time against the qualifying criteria and provide the neccessary Award
if Total_time <= 100 :
    print(f" Your total time is {Total_time} minutes and You've been given the \033[1m Provincial Colours \033[0m Award.") #\033[1m \033[0m makes the text Bold]
elif Total_time <= 105:
    print(f"Your total time is {Total_time} minutes and you've been given the \033[1m Provincial half colours \033[0m Award.")
elif Total_time <= 110:
    print(f"YOur total time is {Total_time} minutes and you have been given the \033[1m Provincial Scroll \033[0m Award.")
else:
    print(f"Your total time is {Total_time} minutes You have \033[1m No award \033[0m ")
