import statistics as st
a = [4,8,9,15,21,21,24,25,26,28,29,34]
#a should be sorted
n = 12#length of a
bins = 3
b = []
for i in range(0,bins):
    c = []
    for j in range(int(i*n/bins),int(i*n/bins)+4):
        c.append(a[j])
    b.append(c)
print('equi-depth bins  ',b)

c = [[0]*int(n/bins) for i in range(bins)]
for i in range(bins):
    d = st.mean(b[i])
    for j in range(int(n/bins)):
        c[i][j] = d
print('smoothing-by-bin-means  ',c)

d = []
for i in range(bins):
    e = []
    for j in range(int(n/bins)):
        if b[i][j]<=c[i][j]:
            e.append(b[i][0])
        else:
            e.append(b[i][int(n/bins)-1])
    d.append(e)
print('smoothing-by-boundary-bins  ',d)

#n-D bins should be converted to 1-D bins



        
    
