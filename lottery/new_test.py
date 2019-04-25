# testCases = int(input())
testCases=1
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
    # line = str(input()).split()
    # cmd = line[0]
    # N = int(line[0])
    N=345487429
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
    print digits
    for i in xrange(0,len(digits)):
        if digits[i] != 4:
            As.append(digits[i]*pow(10,(size-i-1)))
        else:
            As.append(  3 * pow(10, (size-i-1)))
            Bs.append(1 * pow(10, (size-i-1)))

    A=sum(As)
    B=sum(Bs)
    print A
    # my_lst_str = ''.join(map(str, As))
    # print(my_lst_str)
    # print ''.join(str(As))
    # print Bs
    # # end_limit= (4 * pow(10, (size - (index + 1))))-1
    # remainder = N - (4 * pow(10, (size - (index + 1))))
    # r_digits=[int(d) for d in str(remainder)]
    # r_size=len(r_digits)
    # if r_size > 3:
    #     start_n=r_digits[0]
    #     r1= start_n*pow(10,(size-(index+2)))
    #     r2=(r_digits[1]+1)*pow(10,(size-(index+2)))/10
        # start_limit=r1+r2



    # start_limit=50
    # for num in xrange(end_limit, 1, -1):
    # for num in xrange(start_limit,end_limit):
    #         if not is4present(num) and not is4present(N - num):
    #             A = num
    #             B = N - num
    #             break


    print "Case #{}: {} {}".format(testCase, A, B)


