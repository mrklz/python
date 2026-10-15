import helpful_functions
def sum_array(a, k, l):
    i = 0
    sum = 0
    while i < len(a):
        if(i < k or i > l):
            sum += a[i]
        i += 1
    return sum


a = helpful_functions.input_array()
k = int(input())
l = int(input())
print(sum_array(a, k, l))

