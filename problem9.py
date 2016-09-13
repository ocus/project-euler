n = 0
for c in xrange(1000, 1, -1):
    for b in xrange(c, 1, -1):
        for a in xrange(b, 1, -1):
            if a < b < c and a+b+c == 1000 and (a**2 + b**2) == c**2:
                n = (a,b,c)
                break
print(n, reduce(lambda x,y: x*y, n))

