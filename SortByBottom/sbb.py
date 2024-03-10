sentence = "weather is very good today."

words = sentence.split(" ")

words.sort()

print(words)

for i in range(len(words)):
    print(words[i])