import random, math

def median_of_medians(A, i):
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[math.floor(len(sublist)/2)] for sublist in sublists]
    if (len(medians) <= 5):
        v = sorted(medians)[math.floor(len(medians)/2)]
    else:
        v = median_of_medians(medians, len(medians)/2)
    
    sl = [j for j in A if j < v]
    sv = [j for j in A if j == v]   
    sr = [j for j in A if j > v]
    if (i <= len(sl)):
        return median_of_medians(sl, i)
    elif (len(sl) < i <= len(sl) + len(sv)):
        return v
    elif (i > len(sl) + len(sv)):
        return median_of_medians(sr, i - len(sl) - len(sv))


if (__name__ == "__main__"):
    # A = [7, 2, 4, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    # i = 10
    # print(median_of_medians(A, i))

    n = 10000000
    r = 100000
    l = []
    for i in range(n):
        l.append(random.randrange(r))
    print(median_of_medians(l, math.floor(n/2)))
