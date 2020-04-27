

def rotate_matrix(matrix):
	n = len(matrix)

	for i in range(n):
		for j in range(i, n):
			matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

	for i in range(n):
		matrix[i].reverse()

	return matrix

if __name__ == "__main__":
	import sys
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	print(rotate_matrix(matrix))