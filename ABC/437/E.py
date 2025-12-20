from sys import setrecursionlimit

from sortedcontainers import SortedList


def main():
	n = int(input())
	children = [SortedList() for _ in range(n + 1)]
	change = [i for i in range(n + 1)]
	existed = {}
	for i in range(1, n + 1):
		x, y = [int(i) for i in input().split()]
		if (x, y) in existed:
			change[i] = existed[(x, y)]
		else:
			existed[(x, y)] = i

		children[change[x]].add((y, i))

	result = []

	# def dfs(i):
	# 	for j in range(len(children[i])):
	# 		result.append(children[i][j][1])
	# 		if j < len(children[i]) - 1 and children[i][j][0] == children[i][j + 1][0]:
	# 			children[children[i][j + 1][1]].update(children[children[i][j][1]])
	# 		else:
	# 			dfs(children[i][j][1])

	# def dfs(i):
	# 	len_children_i = len(children[i])
	# 	for j in range(len_children_i):
	# 		ij0, ij1 = children[i][j]
	# 		result.append(ij1)
	# 		if j < len_children_i - 1:
	# 			ij10, ij11 = children[i][j + 1]
	# 			if ij0 == ij10:
	# 				# children[ij11].update(children[ij1])
	# 				pass
	# 			else:
	# 				dfs(ij1)
	# 		else:
	# 			dfs(ij1)

	# def dfs(i):
	# 	result.append(i)
	# 	for _, j in children[i]:
	# 		dfs(j)

	def dfs(i):
		current = 0
		while current < len(children[i]):
			result.append(children[i][current][1])
			tmp = current
			while tmp + 1 < len(children[i]) and children[i][tmp][0] == children[i][tmp + 1][0]:
				result.append(children[i][tmp + 1][1])
				tmp += 1
			dfs(children[i][current][1])
			current = tmp + 1

	setrecursionlimit(10 ** 7)
	dfs(0)

	print(*result)


if __name__ == "__main__":
	main()
