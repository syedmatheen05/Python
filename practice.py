arr = [-1,4,-3,0,2,6,-4,-2]
arr.sort()
print(arr)
for i in range(len(arr)):
    left=i+1
    right = len(arr)-1
    while(left < right):
        if arr[i] + arr[left] + arr[right] == 0:
            print(arr[i], arr[left], arr[right])
            break
        elif arr[i] + arr[left] + arr[right] < 0:
            left+=1
        else:
            right-=1