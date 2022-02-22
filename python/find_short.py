# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    s = s.split()
    current = s[0]
    for i in s:
        if len(i) < len(current):
            current = i
    return len(current)

# Examples:
# find_short('bitcoin take over the world maybe who knows perhaps') <- Should return 3
# find_short('turns out random test cases are easier than writing out basic ones') <- Should return 3 aswell