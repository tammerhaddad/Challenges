# given an array A of N integers
# returns the smallest positive integer (greater than 0) that does not occur in A

def mySolution(A):
    s = sorted(A)
    i = 1
    while(i in A):
        i += 1

    return i




















def Solution(A):
    max_val = max(A)
    if max_val < 0:
        return 1
    else:
        all_nums = set(range(1, max_val + 2))
        missing = min(all_nums - set(A))
        return missing