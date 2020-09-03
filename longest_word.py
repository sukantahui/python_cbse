def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

# print(longest_word('myText.txt'))

with open('myText.txt', 'r') as f:
    words = f.read().split()
    print(words)
    print("Number of words {}".format(len(words)))
    max_len = len(max(words, key=len))
    print(max_len)
    print(len('floccinaucinihilipilification'))

    # for line in f:
    #     print(line)
        # if len(line) > large_line_len:
        #     large_line_len = len(line)
        #     large_line = line



