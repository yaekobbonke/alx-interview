#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """is winner"""


    def isPrime(num):
        """is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


    def playGame(n):
        """play game"""
        primes = [num for num in range(2, n+1) if isPrime(num)]
        turn = 0  # 0 for Maria, 1 for Ben
        while n > 1:
            prime = next((p for p in primes if p <= n), None)
            if prime is None:
                break
            n -= prime
            primes = [num for num in primes if num % prime != 0]
            turn = 1 - turn
        return turn

    wins = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = playGame(n)
        if winner is not None:
            wins['Maria' if winner == 0 else 'Ben'] += 1

    max_wins = max(wins.values())
    if wins['Maria'] == wins['Ben']:
        return None
    elif wins['Maria'] > wins['Ben']:
        return 'Maria'
    else:
        return 'Ben'
