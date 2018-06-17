# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
current_region_id = 0
current_region_size = 0
max_region = 0


def print_grid(arr):
    print()
    print("\t\t ", end='')
    for j in range(m):
        print("- {} -\t".format(j), end='')
    print()
    for i in range(m):
        print("- {} -\t".format(i), end='')
        for j in range(n):
            print("{} \t".format(arr[i][j]), end='')
        print()


def check_for_region(arr):
    pass


if __name__ == '__main__':
    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    grid_3d = [[[grid[i][j], 0] for j in range(n)] for i in range(m)]

    print_grid(grid_3d)
    '''
    grid structure:
    
    [1,v] [1,v] [0,v] [0,v]
    [0,v] [1,v] [1,v] [0,v]
    [0,v] [0,v] [1,v] [0,v]
    [1,v] [0,v] [0,v] [0,v]
    
    where is the first value is the original grid value (0 - empty cell, 1 - filled cell)
    the second value is the legend:
    v > 0: indicates the region number
    v = 0: default value, have not been explored yet
    
    '''
    check_for_region(grid_3d)


'''
[0,0]       -> check [0,1][1,0][1,1]
[0,1:n-1]   -> check [1,0][1,1][1,2][0,2]
[0,3]       -> check [1,2][1,3]


'''