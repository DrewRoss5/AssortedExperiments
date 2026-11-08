def coin_change_greedy(coins: list[int], amount: int) -> int:
    coin_count = 0 
    while amount > 0:
        for i in coins:
            if i <= amount:
                amount -= i
                coin_count += 1
                break
    return coin_count
