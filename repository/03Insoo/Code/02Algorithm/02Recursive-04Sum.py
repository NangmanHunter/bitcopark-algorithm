# 재귀합
def sum_recursive(lst):
    if not lst:
        return 0
    else:
        return lst[0]+sum_recursive(lst[1:])

lst=[1,2,3,4,5]
print(lst[1:])
print(sum_recursive(lst))