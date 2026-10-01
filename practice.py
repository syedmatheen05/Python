array =[12,23,134,44,66,90]
target = 89
seen ={}
for i in range(len(array)):
    completed = target - array[i]
    if completed in seen:
        print(array[seen[completed]], array[i])
        break
    seen[array[i]] = i