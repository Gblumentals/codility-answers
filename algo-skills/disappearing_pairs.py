import re

def transform(S, C):
    if len(S) == 1:
        return S

    for k, c in enumerate(C):
        match = re.search(c, S)
        if match != None:
            return transform(S.replace(c, ''), C)
        else:
            if k == len(C)-1:
                return S


def solution(S):
    length = len(S)

    if (length == 0):
        return ''

    m = length // 2

    behind = S[0:m][::-1] # grab string before middle, reverse
    ahead = S[m:length]

    # all palindromes return ''
    if behind == ahead:
        return ''

    U = list(set(S)) # unique characters
    C = []

    #get unique combinations
    for k, u in enumerate(U):
        C.append(u+u)

    result = transform(S, C)

    return result
