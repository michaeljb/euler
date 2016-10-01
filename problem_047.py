#!/usr/bin/env python

from functools import lru_cache

import click

from util import primes


@click.command()
@click.option('-n', '--number', type=int,
              help=('Find this many consecutive integers that have this many '
                    'distinct prime factors.'))
@click.option('-p', '--prime_limit', type=int, default=1e6,
              help=('Calculate all primes less than this number; a list of '
                    'primes must exist before finding prime factors. Defaults '
                    'to 1000000.'))
@click.option('-c', '--cache_size', type=int, default=18,
              help=('Cache the result of get_prime_factors for 2^cache_size '
                    'numbers. Defaults to 18.'))
def main(cache_size, prime_limit, number):
    """The first two consecutive numbers to have two distinct prime factors are:

    \b
    14 = 2 x 7
    15 = 3 x 5

    The first three consecutive numbers to have three distinct prime factors
    are:

    \b
    644 = 2^2 x 7 x 23
    645 = 3 x 5 x 43
    646 = 2 x 17 x 19.

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

    """
    prime_list = primes(prime_limit)

    @lru_cache(maxsize=2**cache_size)
    def get_prime_factors(n):
        for prime in prime_list:
            if n % prime == 0:
                if n == prime:
                    return (n,)
                return (prime,) + get_prime_factors(int(n / prime))

    numbers = list(range(prime_list[0], prime_list[0] + number))

    while True:
        prime_factors = [get_prime_factors(n) for n in numbers]

        if all([len(set(factors)) == number for factors in prime_factors]):
            break

        numbers.pop(0)
        numbers.append(numbers[-1] + 1)

    print(numbers)
    print(prime_factors)


if __name__ == '__main__':
    main()
