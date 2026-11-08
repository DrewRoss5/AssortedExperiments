import sys

from solutions.greedy import coin_change_greedy
from solutions.dynamic import coin_change_dp

def main():
    # read and intialize coins
    if len(sys.argv) < 2:
        print('Error: This program accepts at least one argument', file=sys.stderr)
        return
    coins = []
    try:
        for i in sys.argv[1:]:
            coin_val = int(i)
            coins.append(coin_val)
            if coin_val < 0:
                raise ValueError("")
    except ValueError:
        print('Error: All provided coin values must be positive integers', file=sys.stderr)
        return
    # sort coins in reverse order to simplify greedy search
    coins.sort(reverse=True)
    # find first counterexample
    curr_amount = 1
    while True:
        print(f'Trying {curr_amount}...', end='')
        result_dyn = coin_change_dp(coins, curr_amount)
        result_greedy = coin_change_greedy(coins, curr_amount)
        if result_dyn == result_greedy:
            print('Match')
            curr_amount += 1
        else:
            print(f'Different!\n\tDP: {result_dyn}\n\tGreedy: {result_greedy}')
            return
if __name__ == '__main__':
    main()
    
