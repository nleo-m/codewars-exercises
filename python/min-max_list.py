#Task: Write a function that returns both the minimum and maximum number of the given list/array. 
#The exercise gives only non-empty lists as arguments

def min_max(lst):
    return [min(lst), max(lst)]

#Given tests in codewars exercise:
# test.assert_equals(min_max([1,2,3,4,5]), [1, 5])
# test.assert_equals(min_max([2334454,5]), [5, 2334454])