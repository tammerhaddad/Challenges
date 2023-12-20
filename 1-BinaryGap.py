# Problem: find the length of the longest string of 0s in the binary representation of a number

def mySolution(N):
    # convert to binary
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    # loop through the binary numbers
    for digit in binary:
        if digit == '1':
            # recreates the largest gap
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            # otherwise makes it bigger
            current_gap += 1
    return max_gap
