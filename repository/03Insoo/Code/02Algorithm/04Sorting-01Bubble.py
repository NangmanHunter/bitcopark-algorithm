def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        print(f"Pass{i+1}:{arr}")
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(f"Swap:{arr[j+1]} and {arr[j]} -> {arr}")
    print(f"Final sorted array: {arr}")

arr=[6,0,3,5]
bubble_sort(arr)

                        