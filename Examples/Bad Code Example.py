def f():
    global r
    global c
    if (len(r) < 3):
        nr = r[0] + r[1]
    else:
        nr = r[len(r) - 2] + r[len(r) - 1]
    if nr < c:
        r.append(nr)
        f()
    elif r == c:
        r.append(nr)
r = [0, 1]
c = input()
f()
print(r)