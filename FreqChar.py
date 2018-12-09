from collections import Counter # Python module
import io # enables encoding

file = io.open('article.txt', mode='r', encoding='utf-8')
counter = Counter(file.read().lower().replace(" ", "")) # to convert all characters to lowercase and to remove spaces and to make dictionary of characters and its' frequencies

print("The most frequent character in this article.txt file is " + str(counter.most_common(1)))