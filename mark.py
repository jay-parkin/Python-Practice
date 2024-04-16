# if, else if ladder
# >80 -> distinction
# 60-80 -> first division
# 40-60 -> second division
# <40 -> fail

marks = int(input("Enter your marks: "))

if (marks >= 80):
    print("You got: Distinction")

elif (marks >= 60):
    print("You got: First Division")
    
elif (marks >= 40):
    print("You got: Second Division")

elif (marks < 40):
    print("You got: fail")