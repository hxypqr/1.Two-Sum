
sums=[1,2,3,4,5,7,5,324,5,3]
target=8
i=0
j=0
for i in range(0,7):
    for j in range(0,7):
        if  sums[i]+sums[j]==target:
            print  (i,j)
