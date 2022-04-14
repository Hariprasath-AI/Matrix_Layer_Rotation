import copy 
# Import copy package to use deepcopy function

def matrixRotation(matrix, r):
    
    # This 'deepcopy' function doesn't affect 'matrix' list when changing values in 'temp' list 
    temp = copy.deepcopy(matrix)

    # Initialize start, number of rows and columns
    start = 0
    no_row = len(matrix) - 1
    no_col= len(matrix[0]) - 1
    
    loops = []
    # List 'loops' stores the value of layer and minimum of that is the exact number of layers in the matrix
    loops.append(len(matrix[0]) // 2)
    loops.append(len(matrix) // 2)

    # Rotating 'r' number of times is a time consuming process when rotation(r) is greater than total values(value_count)
    # Example 1: we can take 2 * 2 matrix([1,2],[3,4]), Possible layer count is 1. Number of values in the layer is 4.
    # If we 'r' is greater than number of value(value_count) i.e., For instance value count = 4 , r = 16.
    # Rotating 16 times is a time consuming process for each layer. So our approach is to reduce 'r' by using formula
    # The layer remains the same when 'r' reaches the multiple of value_count i.e., remains same when 'r' value reaches 4, 8, 16.
    # The approach is to get the remainder of dividing 'r' by value_count. If remainder is zero, 'r' is update with remainder value.
    # The loop goes zero times.
    # Example 2: Just changing 'r' from 16 to 17. The updated number of Rotation is 1.
    # Imagine the matrix 300 * 300, r = 999999999(99 crore), 
    # value_count in outer layer is (2 * 300) + (2 * 300) - 4, 1196 values in outer layer.
    # new_rotation = r % value_count
    # new_rotation = 999999999 % 1196
    # Using this approach 99 crore rotations is reduced to 479.     
    value_count = 2 * len(matrix) + 2 * len(matrix[0]) - 4 # FORMULA
    if r > value_count:
        new_rotation = (r % value_count)
    else:
        new_rotation = r

    # Loops through the inner layer of matrix
    for _ in range(0, min(loops)):

        # Loops goes 'r' number of rotations 
        for _ in range(0, new_rotation):

            # These 4 loops goes through the layers of matrix and changes value in anti-clockwise direction
            for i in range(start, no_col ):
                temp[start][i] = matrix[start][i + 1]
            
            
            for j in range(start + 1, no_row + 1):
                temp[j][start] = matrix[j - 1][start]
            

            for k in range(start + 1, no_col + 1):
                temp[no_row][k] = matrix[no_row][k - 1]

            for l in range(start, no_row):
                temp[l][no_col] = matrix[l + 1][no_col]

            matrix = copy.deepcopy(temp)

        # After changing one layer of the matrix, goes to the next layer by
        # 1. increasing start value by 1 
        # 2. decreasing row and column value by 1
        
        start += 1
        no_row -= 1
        no_col -= 1

        # Approach used to reduce number of rotations
        row_val = (no_row  - start) + 1
        col_val = (no_col - start) + 1
        value_count = (2 * row_val) + (2 * col_val ) - 4
        try:
            if r > value_count:
                new_rotation =  r % value_count
            elif r < value_count:
                new_rotation = r
        except:
            continue
        
        
    # Print 2D array each row values in new line and removing commas 
    for i in range(0, len(temp)):
        print(*temp[i])
    

if __name__ == '__main__':
    # First line input consists of m - row, n - column, rotation factor = r
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    # Get line by row input from user for m times and store it in the list 'matrix' 
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    # Call the function 'matrixRotation' and pass the arguments : 1. matrix , 2. r (rotation factor)
    matrixRotation(matrix, r)
