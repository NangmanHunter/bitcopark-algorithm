def dynamic_knapsack(weights, values, capacity):
    n=len(weights)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity + 1):
            if weights[i-1] <=w:
                dp[i][w]=max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
        

    selected_items=[]
    w=capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]

    return dp[n][capacity], selected_items[::-1]



weights=[5,3,4]
values=[70, 40, 50]
capacity=10
max_value, selected_items=dynamic_knapsack(weights, values, capacity)
print(f"최대기치: {max_value}만원")
print("선택된물건:")
total_weight=0
for i in selected_items:
    print(f"물건 {i+1}-무게: {weights[i]}kg, 가치: {values[i]}만원")
    total_weight+=weights[i]
print(f"총무게: {total_weight}kg")





"""
DP정의
ㄴdp[i][w]
ㄴ테이블크기:(물건수+1)ㆍ(최대용량+1)

점화식
ㄴ물건i비선택
dp[i][w]=dp[i-1][w]
ㄴ물건i선택
dp[i][w]=max(dp[i-1][w], dp[i-1][w-weights[i-1]] +values[i-1])

초기값
dp[0][w]=0
dp[i][0]=0




+
문제전제조건
ㄴ한번만담을수있음.


+
selected과정
ㄴ무게를잡고.
ㄴ추가전후
ㄴ같은지를비교해서.
ㄴ같으면->비추가
ㄴ다르면->추가
같은경우->무게그대로
다른경우->무게빼주고
ㄴ즉,
ㄴw라인->좌측이동여부.
ㄴ같음->w그대로
ㄴ다름->w좌측이동

+
결국
ㄴ일단은
ㄴdp테이블
ㄴ이게필하고.
ㄴ여기서
ㄴ모든경우의수
ㄴ다잡은다음.
다잡은것에서.
ㄴ아이템들을
ㄴ역으로추적해서
ㄴ아이템찾는형식.

결론
ㄴDP테이블만들기
ㄴItem역순찾기.
"""