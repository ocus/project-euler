def sort_n(n):
    return ''.join(sorted(list(str(n))))

for n in xrange(1, 1258740):
    sn = sort_n(n)
    if sn == sort_n(n*2) and sn == sort_n(n*3) and sn == sort_n(n*4) and sn == sort_n(n*5) and sn == sort_n(n*6):
        print(n, n*3, n*4, n*5, n*6)
        break
