print("Let's Play Quiz and check your IQ level \n")
score = 0

print("Please Enter the answers in Capital letters \n")

print("Question 1 \n")
que1= input( "What is the full form of IP ? \n"  )

if que1 == "INTERNET PROTOCOL":
    print("correct answer")
    score += 1
else:
    print("Incorrect answer")

print("\n Question 2 \n")

que2= input( "What is the full form of TCP? \n"  )

if que2 == "TRANSMISSION CONTROL PROTOCOL":
    print("correct answer")
    score += 1
else:
    print("Incorrect answer")

print("\n Question 3 \n")

que3= input( "What is the full form of UDP? \n"  )

if que3 == "USER DATAGRAM PROTOCOL":
    print("correct answer")
    score += 1
else:
    print("Incorrect answer")

print("\n Question 4 \n")

que4= input( "What is the full form of SMTP? \n"  )

if que4 == "SIMPLE MAIL TRANSFER PROTOCOL":
    print("correct answer")
    score += 1
else:
    print("Incorrect answer")

print("\n Question 5 \n")

que5= input( "What is the full form of HTTP? \n"  )

if que5 == "HYPER TEXT TRANSFER PROTOCOL":
    print("correct answer")
    score += 1
else:
    print("Incorrect answer")


print("\nYour final score:", score, "out of 5")






