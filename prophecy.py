q1_answer = input("Pick a number 1-10")
q2_answer = input("Choose of the two: ocean or sky")

a1 = False
a2 = False

if int(q1_answer) < 6:
    a1 = True

if q2_answer == "ocean":
    a2 = True


if a1 and a2:
    print("You love the vast blue ocean and wish to work in a sea related industry. You will become successful in doing so.")

elif a1 and not a2:
    print("You love the ocean, but the ocean doesn't love you. It always seems like its trying to make your life miserable.")

elif not a1 and a2:
    print("You love the endless sky with majestic clouds and want to become a pilot. You will become a successful pilot.")

else:
    print("You love the endless sky with majestic clouds and want to become a pilot. However, you will crash multiple planes and end up in massive debt.")