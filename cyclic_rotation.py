# Codility
# While loop to iterate "K" times
# Make a temp array based on "A"
# iterate with a for loop over "A" and make the reemplacements in temp
# if len(A) - 1 should pass to be the first element


def solution(A, K):
    while K != 0:
        temp = A[:]
        for idx, value in enumerate(A):
            if idx == len(temp) - 1:
                temp[0] = value
            else:
                temp[idx + 1] = value
        A = temp
        K -= 1
    return A