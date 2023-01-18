def medal(mytime, time1, time2, time3):
    times = [mytime, time1, time2, time3]
    sorted(times)
    if mytime == times[3]:
        print("You won no medal")
    elif mytime == times[2]:
        print("You won bronze!")
    elif mytime == times[1]:
        print("You won silver!")
    elif mytime == times[0]:
        print("You won gold!")

mytime = input("Enter your time: ")
time1 = input("Enter your opponent's time: ")
time2 = input("Enter your opponent's time: ")
time3 = input("Enter your opponent's time: ")
medal(mytime, time1, time2, time3)
