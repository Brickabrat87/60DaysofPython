#Write a program to flatten a nested list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = []
for row in matrix:
	for element in row:
		new_matrix.append(element)

print(new_matrix)
