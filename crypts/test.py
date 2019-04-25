# t = int(raw_input())  # read a line with a single integer
t=1

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
    alphas= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    return alphas.index(alpha)

def get_prime_till(number,length):
    primes=[]
    for i in xrange(2,number):
        if isPrime(i):
            # if len(primes) < length:
            primes.append(i)

    # return primes[::-1]
    return primes

def get_primeList(number,length,clist,primes,start_prime,allprimes):
    primes=primes

    if len(primes) == 0:
        c = clist[len(primes)]
        allprimes = allprimes
        start_prime=start_prime
        second_prime=None
        second_prime_index=None
    else:
        c = clist[len(primes)-1]

    if len(primes) < 27:
        for i in xrange(start_prime,len(allprimes)-1):
            if c % allprimes[i] == 0:
                start_prime=i
                first_prime=allprimes[i]
                second_prime=c/first_prime
                second_prime_index=allprimes.index(second_prime)
                primes.append(first_prime)
                primes.append(second_prime)
                break

    # primes=allprimes[start_prime:start_prime+length]
    # if start_prime is not None:
                    # if c % i ==0:
                    # start_prime=i
                    # if len(allprimes) < length:
                #     allprimes.append(i)
                #
                # if start_prime is None:
                #     start_prime = i
                #     allprimes.append(i)
                #     # break


                        # allprimes.append(i)
                    # allprimes.append(i)
            # if len(primes) < length:
            #     primes.append(i)

    # return primes[::-1]
    print primes
    if len(primes) ==length:
        return primes
    else:
        get_primeList(number,length,clist,primes,second_prime_index,allprimes)

def getCypherPair(num,primes,alphas):
    primes=primes
    pair=[]
    cypher=[]
    if len(cypher) == 0:
        for i in xrange(0,len(primes)-1):
            if num % primes[i] ==0 :
                first=primes[i]
                second= num / primes[i]
                cypher.append(alphas[primes.index(first)])
                cypher.append(alphas[primes.index(second)])
                break
    else:
        last_index=alphas[len(cypher)]
        first=primes[last_index]
        second=num/primes[last_index]
        # cypher.append(alphas[primes.index(first)])
        cypher.append(alphas[primes.index(second)])
            # break

    print cypher
    return cypher

for i in xrange(1, t + 1):
    # N, L = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    # clist = [int(s) for s in raw_input().split(" ")]
    # N,L=[10000, 25]
    N,L=[103 ,31]

    clist= [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]
    # clist= [3292937, 175597, 18779, 50429, 375469, 1651121, 2102, 3722 ,2376497, 611683, 489059, 2328901, 3150061, 829981, 421301, 76409, 38477 ,291931, 730241, 959821 ,1664197 ,3057407, 4267589 ,4729181 ,5335543]
    # print "Case #{}: {}".format(i)
    # print "Case #{}: {} - {}".format(N, L, clist)
    blank=[]
    allprimes = get_prime_till(N, 26)
    primes=get_primeList(N,26,clist,blank,0,allprimes)
    alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V','W', 'X', 'Y', 'Z']
    primes=blank
    donePrimes = []
    cypher = []
    for c in clist:
        num=c

        if len(cypher) < 2:
            for i in xrange(0, len(primes) - 1):
                first = primes[i]
                index_p =primes.index(first)
                if num % first == 0:
                    second = num / primes[i]
                    donePrimes.append(first)
                    donePrimes.append(second)
                    cypher.append(alphas[primes.index(first)])
                    cypher.append(alphas[primes.index(second)])
                    # print donePrimes
                    break
        else:
            last_index = cypher[len(cypher)-1]
            first = primes[getIndexFor(last_index)]
            second = num / first
            # cypher.append(alphas[primes.index(first)])
            cypher.append(alphas[primes.index(second)])

        # return cypher
    print ''.join(cypher)
