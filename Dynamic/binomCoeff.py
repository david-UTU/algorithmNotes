import functools

functools.lru_cache(None)

def computeBinCoeff(n, k):
    if k in (0, n):
        return 1

    withoutK = computeBinCoeff(n-1, k)
    withK = computeBinCoeff(n-1, k-1)
    return withoutK+withK

print(computeBinCoeff(50, 2))
