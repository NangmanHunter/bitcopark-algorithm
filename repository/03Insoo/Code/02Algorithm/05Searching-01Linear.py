def linear_search(arr, target):
    for i in range(len(arr)):
        print(f"비교중: {arr[i]}와 {target}비교")
        if arr[i]== target:
            return f"값 {target}은 리스트의 {i}번째위치에 있습니다."
    return "찾지못함"

arr=[4,2,7,1,5]
target=7
result=linear_search(arr, target)
print(result)