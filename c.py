def myfunc(n):
    return lambda a: a*n
myn = myfunc(2)
print(myn(11))