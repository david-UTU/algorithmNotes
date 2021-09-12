def lib(n):
    if n <= 1:
        return None
    lib(n-2)
    print('~~~recursion~~~')
    lib(n-2)
    print('~~~recursion~~~')
print(lib(20))