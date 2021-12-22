#First Unique 100%
def solution(A):
    if len(A) == 0:
        return -1

    seen = dict()

    for i in A:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    oc = list(seen.values()) # occurences
    unique = list(seen.keys()) # unique numbers

    try:
        sm = unique[oc.index(1)] # get first unique
        return sm
    except:
        return -1
