def _seq():
    n = 1  # init seq: natural numbers
    while True:
        n += 2  # skip all evens
        yield n


def _not_divisible_by(d):
    return lambda x: (x % d > 0)


def _primes():
    """ apply sieve of Eratosthenes """
    yield 2  # init prime number: 2
    seq = _seq()
    while True:
        p = next(seq)
        yield p  # generate head of seq
        seq = filter(_not_divisible_by(p), seq)  # remove nums divisible by head from seq


def print_primes(end):
    for p in _primes():
        if p <= end:
            print('{0} '.format(p), end='')
        else:
            break


if __name__ == '__main__':
    print_primes(100)
