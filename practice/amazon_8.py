"""
Reverse the order of words in a given sentence (an array of characters).
"""


def reverse_words(sentence):    # sentence here is an array of characters
    result = ""
    stack = []

    for word in sentence:
        stack.append(word)
        stack.append(' ')

    stack.pop()

    while stack:
        result += stack.pop()

    return result

    # word = ""
    # for c in sentence:
    #     if c == ' ':
    #         stack.append(word)
    #         stack.append(' ')
    #         word = ""
    #     else:
    #         word += c
    #
    # stack.append(word)
    #
    # while stack:
    #     result += stack.pop()
    #
    # return result
#

print(reverse_words(['Hello', 'World']))
# print(reverse_words(['H','e','l','l','o',' ','W','O','l','d']))