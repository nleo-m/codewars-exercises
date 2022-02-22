# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)

# Examples:
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    a = arr[0]
    b = None
    Numbers_a = 0
    Numbers_b = 0

    for i in arr:
        if i!=a:
            b = i
            Numbers_b +=1
        else:
            Numbers_a += 1
            
    if Numbers_a > Numbers_b:
        return b
    else:
        return a