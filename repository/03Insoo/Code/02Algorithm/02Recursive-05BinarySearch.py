def binary_search(arr, target, low, high):
    if low>high:
        return -1
    
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high)

sorted_arry=[1,3,5,7,9,11,13,15]
target=7
result=binary_search(sorted_arry,target,0,len(sorted_arry)-1)
print(f"요소{target}은 인덱스{result}에 있습니다.")