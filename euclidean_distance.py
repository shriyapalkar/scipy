from scipy.spatial.distance import euclidean
p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1,p2) #root (x2-x1)2+(y2-y1)2
print(res)