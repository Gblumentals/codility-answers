  def solution(S):
    length = len(S)

    # extremes
    if length == 0:
        return -1

    if (length == 1):
        return 0

    if length % 2 == 0:
        return -1

    m = length // 2

    behind = S[0:m][::-1] # grab string before middle, reverse
    ahead = S[m+1:length]

    if behind == ahead:
        return m

    return -1
