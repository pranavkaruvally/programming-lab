def word_length(s):
    total = 0
    for x in s:
        total += 1
    return total

def longest_word_length(words):
    longest = 0
    for word in words:
        wl = word_length(word)
        if wl > longest:
            longest = wl
    return longest

words = input("Enter words seperated by spaces: ").split()
print("Longest length: %d" %longest_word_length(words))
