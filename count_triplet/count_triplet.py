def countTriplets(arr, r):
    n = len(arr)
    if r == 1:
        return int(n*(n-1)*(n-2)/6)
    d = {}
    for i in arr:
        d[i] = d.get(i,0)+1
    count = 0
    for i in d:
        if i*r in d and i*r*r in d:
            count += d[i]*d[i*r]*d[i*r*r]
    return count

print(countTriplets([1,3,3,3,9,9,9,27,81],3))
