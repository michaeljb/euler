#!/usr/bin/env python

from functools import lru_cache
from pprint import pprint
import sys

import click


# http://stackoverflow.com/a/2068548
# http://stackoverflow.com/a/3035188
@lru_cache(maxsize=128)
def primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * int(n/2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1, int(n/2)) if sieve[i]]


@lru_cache(maxsize=128)
def ways_to_sum_with_primes_to(number):
    ways = set()

    if number < 0:
        return ways

    prime_list = primes(number + 1)

    if number in prime_list:
        ways.add((number,))

    for prime in prime_list:
        for way in ways_to_sum_with_primes_to(number - prime):
            ways.add(tuple(sorted(way + (prime,))))

    return ways


@click.command()
@click.option('-n', '--number', type=int,
              help='Find all the different ways this number can be written as '
              'the sum of primes.')
@click.option('-w', '--ways', type=int,
              help=('Find the first number which can be written as the sum of '
                    'primes in this many ways.'))
@click.option('-p', '--print_list', is_flag=True, default=False,
              help=('Print all the ways the chosen or found number can be '
                    'written as the sum of primes.'))
def main(ways, number, print_list):
    """It is possible to write ten as the sum of primes in exactly five
    different ways:

    \b
    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

    What is the first value which can be written as the sum of primes in over
    five thousand different ways?

    """
    number_set = number is not None
    ways_set = ways is not None

    if not (number_set ^ ways_set):
        print('set either one number or ways')
        sys.exit(1)

    if number_set:
        ways_ = ways_to_sum_with_primes_to(number)
        print(number, len(ways_))

    if ways_set:
        i = 0
        while True:
            ways_ = ways_to_sum_with_primes_to(i)
            if len(ways_) >= ways:
                print(i, len(ways_))
                break
            else:
                i = i + 1

    if print_list:
        pprint(ways_)


if __name__ == '__main__':
    main()
