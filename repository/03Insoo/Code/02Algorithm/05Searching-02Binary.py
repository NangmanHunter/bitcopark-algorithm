def binary__search(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return f"값 {target}은 리스트의 {mid}번째 위치에 있습니다."
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "값을 찾지못했습니다."

arr=[1,3,4,6,8,9,11]
target=3

result=binary__search(arr,target)
print(result)

