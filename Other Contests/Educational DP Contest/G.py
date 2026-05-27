from sys import setrecursionlimit


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	# noinspection DuplicatedCode
	edges_rev = [[] for _ in range(n)]
	for _ in range(m):
		x, y = [int(i) - 1 for i in input().split()]
		edges[x].append(y)
		edges_rev[y].append(x)

	visited = [False] * n
	result = [0] * n

	def dfs(node: int):
		visited[node] = True

		for i in edges_rev[node]:
			if not visited[i]:
				dfs(i)
			result[node] = max(result[node], result[i] + 1)

	setrecursionlimit(10 ** 7)
	for i in range(n):
		if not edges[i]:
			dfs(i)
	print(max(result))


if __name__ == "__main__":
	main()
