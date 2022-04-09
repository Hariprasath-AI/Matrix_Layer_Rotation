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

    # Loops goes 'r' number of rotations 
    for _ in range(0, r):

        # Loops through the inner layer of matrix
        for _ in range(0, min(loops)):

            # These 4 loops goes through the layers of matrix and changes value in anti-clockwise direction
            for i in range(start, no_col ):
                temp[start][i] = matrix[start][i + 1]
            
            
            for j in range(start + 1, no_row + 1):
                temp[j][start] = matrix[j - 1][start]
            

            for k in range(start + 1, no_col + 1):
                temp[no_row][k] = matrix[no_row][k - 1]

            for l in range(start, no_row):
                temp[l][no_col] = matrix[l + 1][no_col]

            # After changing one layer of the matrix, goes to the next layer by
            # 1. increasing start value by 1 
            # 2. decreasing row and column value by 1
            
            start += 1
            no_row -= 1
            no_col -= 1
        
        # Layer starts from the 0 on next iteration. So, reinitializing start value, number of rows, columns and update matrix with the new 'temp' list 
        start = 0
        no_row = len(matrix) - 1
        no_col= len(matrix[0]) - 1
        matrix = copy.deepcopy(temp)

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
