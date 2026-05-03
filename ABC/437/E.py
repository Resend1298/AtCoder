from collections import defaultdict
from sys import setrecursionlimit


def main():
	n = int(input())
	replace_father = {}
	existed_xy = {}
	children = [defaultdict(list) for _ in range(n + 1)]

	for i in range(1, n + 1):
		x, y = [int(i) for i in input().split()]

		if x in replace_father:
			x = replace_father[x]
		if (x, y) in existed_xy:
			replace_father[i] = existed_xy[(x, y)]
		else:
			existed_xy[(x, y)] = i

		children[x][y].append(i)

	result = []

	def dfs(node):
		children[node] = dict(sorted(children[node].items()))

		for v in children[node].values():
			result.extend(v)
			dfs(v[0])

	setrecursionlimit(10 ** 7)
	dfs(0)
	print(*result)


if __name__ == "__main__":
	main()
