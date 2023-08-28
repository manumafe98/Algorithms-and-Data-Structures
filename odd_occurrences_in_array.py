# Crete an empty dict
# iterate over the array
# if value not in dict add it with the idx as value
# if exists delete it
# Only the one with no duplicated values will remain

def solution(A):
    idx_dict = dict()
    for idx, value in enumerate(A):
        if value in idx_dict:
            idx_dict.pop(value)
        else:
            idx_dict[value] = idx
    res = list(idx_dict.keys())[0]
    return res
