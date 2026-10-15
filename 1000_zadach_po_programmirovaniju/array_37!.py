def input_array():
    n = int(input())
    a = list()
    i = 0
    while i < n:
        a.append(int(input()))
        i += 1
    return a 
def nums_up(arr):
    i = 0
    s = 0
    while i < len(arr):
        if(arr[i]>arr[i-1]):
            s += 1
        i += 1
    return s

arr = input_array()
print(nums_up(arr))