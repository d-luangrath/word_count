"""Count words in file."""
import sys

filename = sys.argv[1]
# f = open(filename)
# number_of_word_occurences = {}

#for loop to iterate thru each line to get word
#remove white space at end of line, get words into a list

    #once words are in a list, create for loop to interate thru each word in the given list
    #if word in line(the list of words created)
        #from dict, get the word and default to 0 if not found, otherwise add 1 to count

#when done, for loop to iterate thru items in the list and print the "word" and its "count"

# for line in f:
#     line = line.rstrip().split()
    
#     for word in line:
#         number_of_word_occurences[word] = number_of_word_occurences.get(word, 0) + 1

# for word, count in number_of_word_occurences.items():
#     print(word, count)


def tokenize():
    '''Returns list of words from a file'''
    token = []

    with open(filename) as f:
        for line in f:
            stripped_lines = line.rstrip().split()
            print(type(stripped_lines))
            token.extend(stripped_lines)

    return token

print(tokenize())