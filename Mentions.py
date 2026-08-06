Note1 = float(input("Enter the first note: "))
Note2 = float(input("Enter the second note: "))
Note3 = float(input("Enter the third note: "))
Average = (Note1 + Note2 + Note3) / 3
if Average >= 16 and Average <= 20:
    print("The average of the notes is: ", Average, "Excellent Mention")
elif Average >= 14 and Average < 16:
    print("The average of the notes is: ", Average, "Very Good Mention")
elif Average >= 12 and Average < 14:
    print("The average of the notes is: ", Average, "Good Mention")
elif Average >= 10 and Average < 12:
    print("The average of the notes is: ", Average, "Fair Mention")
elif Average < 10:
    print("The average of the notes is: ", Average, "Insufficient Mention")
else:
    print("Invalid average")