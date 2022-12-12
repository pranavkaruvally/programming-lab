def char_freq(s):
    s = ''.join([x for x in s.lower() if x in 'abcdefghijklmnopqrstuvwxyz'])
    char_freq = dict()
    for x in s:
        if x in char_freq.keys():
            char_freq[x] += 1
        else:
            char_freq[x] = 1
    return char_freq

string = input("Enter a string: ")
print(char_freq(string))
