#You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item)
#and number of people get off the bus (The second item) in a bus stop.
#Task: Return the number of people in the bus after last stop, which can't be 0. 'Even though it is the last bus stop, the bus is not empty and some people are still
#in the bus, and they are probably sleeping there :D'

def number(bus_stops):
    people_in_bus = 0
    i = 0
    for a in bus_stops:
        i = 0
        for b in a:
            if i == 0:
                people_in_bus += b
            elif i == 1:
                people_in_bus -= b
            else:
                break
            i += 1
    return people_in_bus

#Given tests in this codewars exercise:
#test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
#test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
#test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)