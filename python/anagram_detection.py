# Return if a given word is a anagram of another.
# Note: Anagrams are case-insensitive.


def is_anagram(test, original):
    test = test.lower()
    original = original.lower()

    if len(original) != len(test):
        return False

    for i in test:
        if i not in original:
            return False
    for i in original:
        if i not in test:
            return False

    return True


# Examples:
#  "foefet" is an anagram of "toffee"
#  "Buckethead" is an anagram of "DeathCubeK"
