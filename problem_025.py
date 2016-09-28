#!/usr/bin/env python

from functools import lru_cache

import click


@lru_cache(maxsize=4)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@click.command()
@click.option('-l', '--length', type=int,
              help=('Find the index of the first term in the Fibonacci sequence '
                    'with this many digits.'))
@click.option('-p', '--print_num', is_flag=True, default=False,
              help=('Print the fibonacci number found at that index.'))
def main(length, print_num):
    """
    The Fibonacci sequence is defined by the recurrence relation:

    \b
    F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

    Hence the first 12 terms will be:

    \b
    F_1 = 1
    F_2 = 1
    F_3 = 2
    F_4 = 3
    F_5 = 5
    F_6 = 8
    F_7 = 13
    F_8 = 21
    F_9 = 34
    F_10 = 55
    F_11 = 89
    F_12 = 144
    The 12th term, F_12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    i = 0
    while True:
        number = fib(i)
        if len(str(number)) >= length:
            break
        i = i + 1

    print(i)

    if print_num:
        print(number)


if __name__ == '__main__':
    main()
