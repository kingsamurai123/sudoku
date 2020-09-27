# import time

def isSafe(arr):
	print("Started Safe phase")
	# flag = 0
	for i in range(N):
		for j in range(N):
			ans = arr[i][j]
			if ans > 10:
				print("Invalid number")
				return False         #main file code
				# flag = 1
				# break     
			else:
				for ii in range(N):
					if ( j != ii and ans == arr[i][ii] ) or ( i != ii and ans == arr[ii][j]):
						return False           #main file code
						# flag = 1
						# break
	return True         #main file code
	# if flag == 1:
	# 	print("FAILED")
	# else:
	# 	print("GRAND SUCCESS")



def printGrid(grid):
	print("Started Printing")
	for row in range(N):
		for col in range(N):
			print(grid[row][col],end=" ")
		print()


def solveSudoku(grid, i, j):
	print("Started Solving")
	if i == N-1 and j == N:
		if isSafe(grid):
			printGrid(grid)
			return True
		return False
	if j == N:
		i = i+1
		j = 0
	if grid[i][j] != UNASSIGNED:
		return solveSudoku(grid , i, j + 1)
	for num in range(1,10):
		grid[i][j] = num
		if solveSudoku(grid , i , j + 1):
			return True
		grid[i][j] = 0
	return False

# start = time.time()

UNASSIGNED = 0
N = 9

grid = [
[3,1,6,5,7,8,4,9,2],
[5,2,9,1,3,4,7,6,8],
[4,8,7,6,2,9,5,3,1],
[0,0,0,0,0,5,9,8,7],
[9,7,4,8,6,3,1,2,5],
[8,5,1,7,9,2,6,4,3],
[1,3,8,9,4,7,2,5,6],
[6,9,2,3,5,1,0,7,4],
[7,4,5,2,8,6,3,1,9]
]

if solveSudoku(grid , 0, 0) != True:
	print("No solution exists")


# end = time.time()

# print(f"Execution time {end-start}")