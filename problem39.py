p = 1000
maximized_p = None
maximized_solutions = set()
for p in range(1, 1001):
    print('Checking %s' % p)
    sp = p / 2
    p_solutions = set()
    for a in range(1, sp + 1):
        for b in range(1, sp + 1):
            if (a**2 + b**2) == (p - a - b)**2:
                solution = (a, b, int((a**2 + b**2)**.5))
                p_solutions.add(tuple(sorted(solution)))
    if len(p_solutions) > len(maximized_solutions):
        maximized_p = p
        maximized_solutions = p_solutions

print('=> Maximized for %s (%s)' % (maximized_p, maximized_solutions))
