time=int(input("enter time (0-23): "))
if 5<=time<=10:
    print("Breakfast time")
elif 12<=time<=15:
    print("Lunch time")
elif 19<=time<=22:
    print("Dinner time")
else:
    print("It's not a meal time")