t = int(raw_input())  # read a line with a single integer


def isPrime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:

            return True
    else:
        return False


def getIndexFor(alpha):
    alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V',
              'W', 'X', 'Y', 'Z']
    return alphas.index(alpha)


def get_prime_till(number, length):
    primes = []
    number = number + 2
    for i in xrange(2, number):
        if isPrime(i):
            # if len(primes) < length:
            primes.append(i)

    return primes


for tc in xrange(1, t + 1):
    N, L = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    clist = [int(s) for s in raw_input().split(" ")]

    alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

    primes = get_prime_till(N, len(alphas))

    donePrimes = []
    cypher = []
    new_primes = []

    for prime in primes:
        for c in clist:
            if c % prime != 0:
                pass
            else:
                if prime not in new_primes:
                    new_primes.append(prime)


    primes = new_primes

    for c in clist:
        num = c
        if len(cypher) == 0:
            for i in xrange(0, len(primes) - 1):
                if num % primes[i] == 0:
                    first = primes[i]
                    second = num / primes[i]
                    donePrimes.append(first)
                    donePrimes.append(second)
                    cypher.append(alphas[primes.index(first)])
                    cypher.append(alphas[primes.index(second)])
                    # print donePrimes
                    break
        else:
            last_index = cypher[len(cypher) - 1]
            first = primes[getIndexFor(last_index)]
            second = num / first
            # cypher.append(alphas[primes.index(first)])
            cypher.append(alphas[primes.index(second)])

    result = ''.join(cypher)
    print "Case #{}: {}".format(tc, result)