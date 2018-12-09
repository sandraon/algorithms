import io # enables encoding

file = io.open('article.txt', mode='r', encoding='utf-8')

text = file.read().replace(" ", "").lower()

def find_most_freq_char():
    counter = 0
    total_counter = 0
    most_freq_char = ""

    for ch in text:
        for str in text:
            if str == ch:
                counter += 1

        if counter > total_counter:
            total_counter = counter
            most_freq_char = ch
        counter = 0

    print("The most frequent character is", most_freq_char, "and it appears", total_counter, "times.")

find_most_freq_char()