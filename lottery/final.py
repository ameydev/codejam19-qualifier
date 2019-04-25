testCases = int(input())

def is4present(number):
    try:
        digits=[int(d) for d in str(number)]
        if 4 in digits:
            return True
        else:
            return False
    except Exception as e:
        return False


def get4index(number):
    digits=[int(d) for d in str(number)]
    digits.index(4)

for testCase in range(1, testCases + 1):
    line = str(input()).split()
    # cmd = line[0]
    N = int(line[0])
    # a = [float(x) for x in line[2:]]
    A=None
    B=None
    # N = int(raw_input(i))
    start_limit=1
    digits=[int(d) for d in str(N)]

    # if len(digits) > 2:
    index=digits.index(4)
    size = len(digits)
    As=[]
    Bs=[]
    for i in xrange(0,len(digits)):
        if digits[i] != 4:
            As.append(digits[i]*pow(10,(size-i-1)))
        else:
            As.append(  3 * pow(10, (size-i-1)))
            Bs.append(1 * pow(10, (size-i-1)))

    A=sum(As)
    B=sum(Bs)

    print "Case #{}: {} {}".format(testCase, A, B)
