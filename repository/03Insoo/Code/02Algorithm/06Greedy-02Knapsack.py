def greedy_knapsack(weights, values, capacity):
    items=sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)

    total_value=0
    total_weight=0

    for weight, value in items:
        if total_weight + weight<= capacity:
            total_weight+=weight
            total_value+=value
            print(f"물건선택-무게:{weight}kg, 가치: {value}만원, 현재총무게:{total_weight}kg, 총가치:{total_value}만원")
        else:
            print(f"물건선택불가-무게:{weight}kg (용량초과)")

    return total_value

weights=[5,3,4]
values=[70,40,50]
capacity=10

max_value=greedy_knapsack(weights, values, capacity)
print(f"\n그리디알고리즘으로얻은 최대가치: {max_value}만원")