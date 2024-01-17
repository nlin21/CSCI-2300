import random, math, statistics

def selection(S, k):
    v = S[random.randrange(len(S))]
    sl = []
    sv = []
    sr = []
    for i in range(len(S)):
        if (S[i] < v):
            sl.append(S[i])
        elif (S[i] == v):
            sv.append(S[i])
        else:
            sr.append(S[i])
    if (k <= len(sl)):
        return selection(sl, k)
    elif (len(sl) < k <= len(sl) + len(sv)):
        return v
    elif (k > len(sl) + len(sv)):
        return selection(sr, k - len(sl) - len(sv))

if (__name__ == "__main__"):
    # A = [7, 2, 4, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    # k = 10
    # print(selection(A, k))

    # # If the list has even length, there are two choices for what the middle element 
    # # could be, in which case we pick the smaller of the two, say.
    n = 10000000
    r = 100000
    l = []
    for i in range(n):
        l.append(random.randrange(r))
    print(selection(l, math.floor(n/2)))