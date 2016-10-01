My solutions to [Project Euler](https://projecteuler.net/) problems.

All files can be executed to calculate the solution, and take `--help` for more
details. For example:

```
> ./problem_077.py --help
Usage: problem_077.py [OPTIONS]

  It is possible to write ten as the sum of primes in exactly five different
  ways:

  7 + 3
  5 + 5
  5 + 3 + 2
  3 + 3 + 2 + 2
  2 + 2 + 2 + 2 + 2

  What is the first value which can be written as the sum of primes in over
  five thousand different ways?

Options:
  -n, --number INTEGER  Find all the different ways this number can be written
                        as the sum of primes.
  -w, --ways INTEGER    Find the first value which can be written as the sum
                        of primes in this many ways.
  -p, --print_list      Print all the ways the chosen or found number can be
                        written as the sum of primes.
  --help                Show this message and exit.
```

### Requirements to run Python solutions

* Python 3
* [click](http://click.pocoo.org/)
  ([pypi](http://pypi.python.org/pypi/click),
  [conda-forge](https://anaconda.org/conda-forge/click))

### Solved

[25 - 1000-digit Fibonacci number](https://projecteuler.net/problem=25)
```
./problem_025.py --help
./problem_025.py -l 3
./problem_025.py -l 1000
```

[47 - Distinct primes factors](https://projecteuler.net/problem=47)
```
./problem_047.py --help
./problem_047.py -n 2
./problem_047.py -n 3
./problem_047.py -n 4
```

[77 - Prime summations](https://projecteuler.net/problem=77)
```
./problem_077.py --help
./problem_077.py -n 10 -p
./problem_077.py -w 5001
```
