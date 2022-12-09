from collections import Counter

file = open('text_1.txt').read()
counter = Counter(file.split())
words = counter.most_common(5)
print(words)




