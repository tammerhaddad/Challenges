# given an array A consisting of N integers (guaranteed to be paired with one unique), returns the value of the unpaired element.

# this works but is too slow
def mySolution(A):
    unpaired_element = 0
    for num in A:
        # if weve seen it then remove it
        if num in unpaired_element:
            unpaired_element.remove(num)
        else:
            # if we havent then keep it
            unpaired_element.append(num)
    # return the only number left in the list
    return unpaired_element[0]


def Solution(A):
    unique = 0
    for num in A:
        # uses XOR (researched but still dont get it)
        unique ^= num
    return unique

