
# t = int(raw_input())  # read a line with a single integer
t=1

def get_path(cursor,moves,size):
    path=str(moves)
    cursor_new=None
    trace=[cursor]
    diff=[]

    for move in path:
        var = None
        print move
        if move is 'S':
            cursor_new=cursor
            # cursor = cursor+size
            var=size
            # print cursor
        elif move is 'E':
            cursor_new = cursor
            var=1

        cursor = cursor + var

        trace.append(cursor)
        diff.append(var)
        # cursor=cursor_new
    print 'Lydia -- ',trace
    print diff
    return diff

def create_path(cursor,diff,size):
    myPath =[]
    for var in diff:
        if var == size:
            myPath.append('E')
        else:
            myPath.append('S')
    print "".join(myPath)

for i in xrange(1, t + 1):
    # m = [int(s) for s in raw_input().split(" ")][0]  # read a list of integers, 2 in this case
    # n = [s for s in raw_input().split(" ")][0]
    m = 2
    n = 'SE'
    # print "Case #{}: {} - {}".format(i, m, n)
    size_of_matrix=m
    number_of_cells=m*m
    start_point=1
    diff=get_path(start_point,n,size_of_matrix)
    create_path(start_point,diff,size_of_matrix)
    print n
