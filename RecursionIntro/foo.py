def foo(n):
    if n <= 1:
        return None
    else:
        print('~~~recursion~~~')
        return foo(n-1)

print(foo(5))