def is_palindrome(n):
    m = list(str(n))
    m.reverse()
    return int(''.join(m)) == n


# squares = [i**2 for i in xrange(2, 10**3)]
def palindromic_sum(n):
    # s = [i**2 for i in range(2, int(n**.5) + 1)]
    m = int(n**.5) + 1
    for i in xrange(1, m):
        s = i**2
        for j in xrange(i + 1, m):
            s += j**2
            if s == n:
                return range(i, j + 1)
            if s > n:
                break
    return None

s = []
for n in xrange(0, 10**8 + 1):
    if is_palindrome(n):
        ps = palindromic_sum(n)
        if ps:
            s.append(n)
            print(n, ps, sum([i**2 for i in ps]))

print(len(s), 'sum', sum(s))
