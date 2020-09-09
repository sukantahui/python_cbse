


file = open('myTextFile.txt', "r")
content = file.read().split()
maxWordLength=0
maxWord=""
for word in content:
    if len(maxWord)<len(word):
        maxWord =  word
print(maxWord)


file.close()
