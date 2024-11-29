list_1 = [15,1,8,15]
len1 = len(list_1)
p1= 0
p2 = len1-1
flag=0
count=0
for i in range ((len1//2)):
    if (list_1[p1] != list_1[p2]):
        list_1[p1] +=list_1[p1+1]
        count+=1
    p1+=1
    p2-=1
    i +=1
print("minimum number if operations=", count)

