# Python3 program to solve Rat in a Maze
# problem using backtracking

# Maze size
N = 4

# A utility function to print solution matrix sol
def printSolution( sol ):
	
	for i in sol:
		for j in i:
			print(str(j) + " ", end ="")
		print("")

# A utility function to check if x, y is valid
# index for N * N Maze
def isSafe( maze, x, y ):
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False

""" This function solves the Maze problem using Backtracking.
	It mainly uses solveMazeUtil() to solve the problem. It
	returns false if no path is possible, otherwise return
	true and prints the path in the form of 1s. Please note
	that there may be more than one solutions, this function
	prints one of the feasable solutions. """
def solveMaze( maze ):
	
	# Creating a 4 * 4 2-D list
	sol = [ [ 0 for j in range(4) ] for i in range(4) ]
	
	if solveMazeUtil(maze, 0, 0, sol) == False:
		print("Solution doesn't exist")
		return False
	
	printSolution(sol)
	return True
	
# A recursive utility function to solve Maze problem
def solveMazeUtil(maze, x, y, sol):
	
	if x == N - 1 and y == N - 1:
		sol[x][y] = 1
		return True
		
	
	if isSafe(maze, x, y) == True:
		
		sol[x][y] = 1
		
	
		if solveMazeUtil(maze, x + 1, y, sol) == True:
			return True
			
	
		if solveMazeUtil(maze, x, y + 1, sol) == True:
			return True
		
	
		sol[x][y] = 0
		return False


if __name__ == "__main__":
	
	maze = [ [1, 0, 0, 0],
			[1, 1, 0, 1],
			[0, 1, 0, 0],
			[1, 1, 1, 1] ]
			
	solveMaze(maze)


