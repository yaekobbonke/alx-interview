#!/usr/bin/python3
"""
Prime Game
"""


def generate_primes(n):
    """
    generate primes
    """
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    for p in range(int(n ** 0.5) + 1, n + 1):
        if sieve[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    winner = None
    max_wins = 0

    for i in range(x):
        n = nums[i]
        primes = generate_primes(n)
        current_player = 0  # 0 for Maria, 1 for Ben
        can_move = True

        while can_move:
            can_move = False
            for prime in primes:
                if prime <= n:
                    n -= prime
                    can_move = True
                    current_player = 1 - current_player  # Switch players
                    break

        if current_player == 0:
            wins = nums.count(nums[i])
            if wins > max_wins:
                max_wins = wins
                winner = "Maria"
        else:
            wins = nums.count(nums[i])
            if wins > max_wins:
                max_wins = wins
                winner = "Ben"

    return winner
