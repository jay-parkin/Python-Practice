# Fart Butt -> dairyfart
# enter first and last name and company

# first_name -> snake_case -> used for variables in python
# firstName -> camelCase -> used for variables in javascript
# FirstName -> PascalCase -> used for class names in almost all languages
# first-name -> kebab-case -> I don't know where it is used

# fname = input("Enter Firstname: ")
# lname = input("Enter Lastname: ")
# company = input("Enter Company: ")
# email = f"{fname}.{lname}@{company}.com.au"
# print(f"Email: {email}")

# full_name = input("Enter Full name: ")
# company = input("Enter Company: ")

# split_full_name = full_name.split() # ['John', 'Smith']
# full_name = ".".join(split_full_name) # John.Smith

# split_company = company.split() # ['Dairy', 'Farm']
# company = "".join(split_company) # DairyFarm

# email = f"{full_name}@{company}.com.au".lower()
# print(f"Email: {email}")

full_name = input("Enter Full name: ")
company = input("Enter Company: ")

full_name = full_name.replace(" ", ".")
company = company.replace(" ", "")

email = f"{full_name}@{company}.com.au".lower()
print(f"Email: {email}")