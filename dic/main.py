from dic.gride import gride

##a = magnites([[1, 1]], [[1, 2], [2, 2], [1, 3]], [[3, 3]])
b = gride(3, 4, [[2, 0]], [[1, 2]], [[1, 1]], [[1, 3]])
c = b.make_gride()
for row in c:
    print(" ".join(row))
b.start_play()