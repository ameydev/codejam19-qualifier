# testCases = int(input())

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
testCases=1

for testCase in range(1, testCases + 1):
    # line = str(input()).split()

    # N = int(line[0])
    N=4240990004
    if (N is not 0):
        A=None
        B=None
        start_limit=1
        end_limit = N
        digits=[int(d) for d in str(N)]

        index=digits.index(4)
        size = len(digits)
        if index != size :
        # end_limit= (4 * pow(10, (size - (index + 1))))-1

            remainder = N - (4 * pow(10, (size - (index + 1))))
            if remainder != 0:
                r_digits=[int(d) for d in str(remainder)]
                r_size=len(r_digits)
                r_digits = [int(d) for d in str(remainder)]
                r_size = len(r_digits)
                start_n = r_digits[0]
            # print 'r size ', r_size
            # print 'r start_n ', start_n * pow(10, r_size)
            # print size-(index+2)
            # print (r_digits[0] + 1) * pow(10, r_size - 1)
                start_limit=(r_digits[0] + 1) * pow(10, r_size - 1)
                start_limit=(start_limit+end_limit)/2

            # if r_size >3:
            #     start_n=r_digits[0]
            #     r1= start_n*pow(10,(size-(index+2)))
            #     r2=(r_digits[1]+1)*pow(10,(size-(index+2)))/10
            #     start_limit=r1+r2



        for num in xrange(start_limit,end_limit):
            if not is4present(num) and not is4present(N - num):
                A = num
                B = N - num
                break


        print "Case #{}: {} {}".format(testCase, A, B)


