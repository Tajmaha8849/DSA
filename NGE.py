arr=[100,24,24,1,5]
max_arr,lst=[],[]
for i in range(0,len(arr)):
    j=arr[i]
    if(i==(len(arr)-1)):
        lst.append(-1)
        break
    else:
        for k in range(i+1,len(arr)):
            if(j<arr[k]):
                max_arr.append(arr[k])
            else:
                max_arr.append(-1)
    lst.append(min(max_arr))
    max_arr=[]
print(lst)
    