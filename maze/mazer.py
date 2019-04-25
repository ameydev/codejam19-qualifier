t = int(raw_input())  # read a line with a single integer
def get_path(cursor,moves,size):
    path=str(moves)
    diff=[]

    for move in path:
        var = None
        if move is 'S':
            var=size
        elif move is 'E':
            var=1
        diff.append(var)

    return diff

def create_path(cursor,diff,size):
    myPath =[]
    for var in diff:
        if var == size:
            myPath.append('E')
        else:
            myPath.append('S')
    result= "".join(myPath)
    return result

for i in xrange(1, t + 1):
    m = [int(s) for s in raw_input().split(" ")][0]  # read a list of integers, 2 in this case
    n = [s for s in raw_input().split(" ")][0]
    size_of_matrix=m
    number_of_cells=m*m
    start_point=1
    diff=get_path(start_point,n,size_of_matrix)
    result=create_path(start_point,diff,size_of_matrix)

    print "Case #{}: {}".format(i, result)
