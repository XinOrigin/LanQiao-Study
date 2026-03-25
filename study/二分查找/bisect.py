# def bisect (a,x,lo=0,hi=None):
#     if hi is None:hi=len(a)
#     while lo<hi:
#         i = (lo+hi) >> 1
#         if a[i] > x:
#             hi = i
#         else:
#             lo = i + 1
#     return lo 


def bisect (a,x,lo=0,hi=None,check = lambda y : y):
    if hi is None:hi=len(a)
    while lo<hi:
        i = (lo+hi) >> 1
        if check(a[i]) > x:
            hi = i
        else:
            lo = i + 1
    return lo 