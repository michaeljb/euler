#!/usr/bin/env python

import click

from util import primes


def has_even_digit(number):
    return any(digit in str(number) for digit in '02468')


def rotations(number):
    numbers = {number}
    digits = [char for char in str(number)]
    for i in range(len(digits) - 1):
        digits.append(digits.pop(0))
        numbers.add(int(''.join(digits)))
    return sorted(numbers)


@click.command()
@click.option('-l', '--limit', type=int,
              help=('Find the number of circular primes below this number. '
                    'Defaults to 1000000.'))
@click.option('-p', '--print_list', is_flag=True, default=False,
              help=('Print all the found circular primes.'))
def main(limit, print_list):
    """The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?

    """

    prime_list = primes(limit)
    is_circular = {}
    circular_primes = [2]

    for prime in prime_list:
        if has_even_digit(prime) or (is_circular.get(prime) in [True, False]):
            continue

        numbers = rotations(prime)

        indices = []
        prime_is_circular = True
        for num in numbers:
            try:
                indices.append(prime_list.index(num))
            except ValueError:
                prime_is_circular = False

        if prime_is_circular:
            circular_primes += numbers

        for num in numbers:
            is_circular[num] = prime_is_circular

    print(len(circular_primes))
    if print_list:
        print(circular_primes)


if __name__ == '__main__':
    main()
