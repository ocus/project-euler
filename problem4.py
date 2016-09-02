def is_palindrome(n):
	n = str(n)
	l = len(n)
	for i in xrange(int(l / 2) + (l % 2 > 0)):
		a = n[i]
		b = n[-1+-i]
		if a != b:
			return False
	return True

n = []
for i in xrange(1000, 100, -1):
	for j in xrange(1000, i, -1):
		if is_palindrome(i*j):
			n.append(i*j)

print(max(n))

