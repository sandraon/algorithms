import sys
import string
import io # enables encoding

# Opening and reading file article.txt
file = io.open('article.txt', mode='r', encoding='utf-8')

with file as f:
    found = []
    longest = ""
    for line in f:
        for character in line:
            if character.lower().isalpha() and character.lower() not in found:
                found.append(character.lower())
            else:
                if len(found) > len(longest):
                    longest = "".join(found)
                found = []
    print ("Longest string found: " + str(longest))