# http://stackoverflow.com/a/2068548
# http://stackoverflow.com/a/3035188
def primes(n):
    """ Returns a list of primes < n """
    sieve = [True] * int(n/2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1, int(n/2)) if sieve[i]]
