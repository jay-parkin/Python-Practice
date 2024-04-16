readme_file = open("readme.txt")

words = readme_file.read().split()


readme_file.close()

print(words)