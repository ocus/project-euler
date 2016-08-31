f = [1,2]
s = 3
while s < 4000000:
    f.append(s)
    s = sum(f[-2:])
    
print(sum([i for i in f if i % 2 == 0]))
