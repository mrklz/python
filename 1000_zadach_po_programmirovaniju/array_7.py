n = int(input())
a = list()
i = 0
while i < n:
    a.append(int(input()))
    i += 1 
while i > 0:
    print(a[i - 1])
    i-=1