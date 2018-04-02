g1 = 'test', 'testq', 'wqddqdq'
a = 0
for y in range(len(g1)):
    l=list(g1[y])
    for x in l: a+=ord(x)
print(a)
