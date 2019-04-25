def is4present(number):
    try:
        digits=[int(d) for d in str(number)]
        if 4 in digits:
            return True
        else:
            return False
    except Exception as e:
        return False
def r_plus(r):
    r = r+1
    return r

def get4index(number,r):
    digits=[int(d) for d in str(number)]
    size=len(digits)
    index=digits.index(4)
    print 'number--',number
    print 'index--',index+1
    print 'size--',size
    print 'value at index = ',(4*pow(10,(size-(index+1))))
    end_limit = (4 * pow(10, (size - (index + 1)))) - 1
    print 'For loop should end with, ',end_limit
    remainder=number-(4*pow(10,(size-(index+1))))

    print 'remainder--',remainder
    r_digits=[int(d) for d in str(remainder)]
    r_size=len(r_digits)
    start_n=r_digits[0]
    print 'r size ',r_size
    print 'r start_n ', start_n*pow(10,r_size)
    # print size-(index+2)
    print (r_digits[0]+1)*pow(10,r_size-1)
    # print 'r start_n+1 ', (r_digits[1]+1)*pow(10,r_size)/10
    # print 'start_number = ',start_n*pow(10,r_size)+(r_digits[1]+1)*pow(10,r_size)/10
    # if is4present(remainder):
    #     r = r+1
    #     print '========for recursion number =========',r
    #     get4index(remainder,r)
    # # my_lst = digits[index+1:]
    # my_lst_str = ''.join(map(str, my_lst))
    # print('start ... ',my_lst_str)


# get4index(4234567890)
# get4index(4444444444)
r=0
# get4index(4523056749,0)
get4index(404030,0)
# start_limit=10
# end_limit=1
# start_limit = (start_limit + end_limit) / 2
#
# print start_limit