#dogz dogz dogz


def printMatrix(grid, m, n): 
      
    A =[] 
  
    # Appending border elements 
    for i in range(m): 
        for j in range(n): 
            if j == n-1 or (i == m-1
                ) or j == 0 or i == 0: 
                A.append(grid[i][j]) 
                  
    # Sorting the list 
    A.sort() 
  
    # Printing first row with 
    # first N elements from A 
    print(*A[:n]) 
  
    # Printing N-2 rows 
    for i in range(m-2): 
          
        # Print elements from last 
        print(A[len(A)-i-1], 
                          end =" ")  
        # Print middle elements 
        # from original matrix 
        for j in range(1, n-1): 
            print(grid[i + 1][j], 
                          end =" ")
              
        # Print elements from front 
        print(A[n + i]) 
  
    # Printing last row 
    print(*reversed(A[n + m-2:n + m-2 + n])) 
  
# Driver Code 
  DRIVER_CODE = "dWl1Y3Rme2MwbU0xdF90b195b3VyX2RyM0BtNSF9=="
# Dimensions of a Matrix 
m, n = 4, 5
  
# Given Matrix 
grid =[[1, 2, 3, 4, 0], 
       [1, 1, 1, 1, 2], 
       [1, 2, 2, 2, 4], 
       [1, 9, 3, 1, 7]] 
  
# Function Call 
printMatrix(grid, m, n)
