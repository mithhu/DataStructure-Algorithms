def nextGreater(A):
    s = []
    v = []
    for i in (range(len(A))):
        if len(s) == 0:
            v.append(-1)
        elif len(s) > 0 and s[-1][0] > A[i]:
            v.append(s[-1][1])
        elif len(s) > 0 and s[-1][0] <= A[i]:
            while len(s) > 0 and s[-1][0] <= A[i]:
                s.pop()
            if len(s) == 0:
                v.append(-1)
            else:
                v.append(s[-1][1])
        s.append((A[i], i))
    return v


print(nextGreater([100, 120, 80]))
