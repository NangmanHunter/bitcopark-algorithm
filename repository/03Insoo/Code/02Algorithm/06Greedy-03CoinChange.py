def coin_change(coins, amount):
    coins.sort(reverse=True)
    coin_count=0
    details=[]

    for coin in coins:
        if amount==0:
            break
        count=amount//coin
        coin_count+=count
        amount-=count*coin
        if count>0:
            details.append((coin, count))
    
    if amount !=0:
        return "정확하게 거슬러줄수없습니다."

    result=f"최소동전개수: {coin_count}개\n"
    for coin, count in details:
        result += f"{coin}원동전 {count}개\n"
    
    return result


coins=[10,7,1]
amount=14
print(coin_change(coins, amount))
