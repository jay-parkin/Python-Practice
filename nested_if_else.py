# 2 states - State1 and State2 - take input from the user
state = input("Enter your state: ")

# take age as input from the user
age = int(input("Enter your age: "))

# In State1,
# age >= 18, can vote
# age < 18, cannot vote

# In State2,
# age >= 20, can vote
# age < 20, cannot vote

if (state == "State1"):
    if (age >= 18):
        print("Can vote")
    else:
        print("Cannot vote")
else: # State3
    if (age >= 20):
        print("Can vote")
    else:
        print("Cannot vote")