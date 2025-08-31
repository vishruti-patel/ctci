"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""


def word_pattern(pattern, word):
    # word = word.split(' ')

    d = { }

    if len(pattern) != len(word):
        return False
    if len(set(pattern)) != len(set(word)):
        return False
    # print(set(pattern), set(word))

    for w, p in zip(word, pattern):
        if w not in d:
            d[w] = p
        elif w in d:
            if d[w] != p:
                return False
    return True

is_word_pattern = word_pattern('abab', 'cat dog cat dog')
is_word_pattern_1 = word_pattern('abba', 'hey hi hi hey')

if word_pattern:
    print("It's a pattern")
else:
    print("Not a pattern")

if is_word_pattern_1:
    print("It's a pattern")
else:
    print("Not a pattern")