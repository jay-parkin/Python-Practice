# len
# lower
# upper
# split
# join
# replace

name = "Steven Smith"
print(len(name))
print(name.lower())
print(name.upper())

print(name.split())
list = name.split() # ['Steven', 'Smith']

print(" ".join(list))
print(name.replace(name, name[::-1]))

