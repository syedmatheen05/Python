arr = [1,2,3,4]
new_arr =[]
for i in range(len(arr)):
    product =1
    for j in range(len(arr)):
        if i == j :
            continue
        product*=arr[j]
    new_arr.append(product)
print(new_arr)
        
