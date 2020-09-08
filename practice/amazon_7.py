"""
You are given a dictionary of words and a large input string.
You have to find out whether the input string can be completely segmented into the words of a given dictionary.
The following two examples elaborate on the problem further.
"""


def can_segment_string(s, dictionary):
    for i in range(1, len(s)+1):
        first = s[0:i]
        second = s[i:]

        if first in dictionary and second in dictionary:
            return True

    return False

    # for word in dictionary:
    #     if not s:
    #         break
    #     if word in s:
    #         s = s.replace(word, '')
    #
    # if s:
    #     return False
    # else:
    #     return True


print(can_segment_string("hellonow", {'on', 'hello', 'now', 'hell'}))