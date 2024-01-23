# Rotate array A K times; that is, each element of A will be shifted to the right K times.

def mySolution(A, K):
    # copy so i dont overwrite
    temp = A.copy()
    l = len(A)
    # loops through A
    for i in range(l):
        # changes the corresponding number in temp
        temp[(i+K)%l] = A[i]
    # returns final solution
    return temp


# failed some tests but simpler so i like it
# def myOtherSolution(A, K):
#     l = len(A)
#     return [A[abs(l-K+i)%l] for i in range(l)]