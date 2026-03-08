from sys import setrecursionlimit


def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(n - 1):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)

	visited = [False] * n
	visited_a = set()
	result = [False] * n

	def dfs(i):
		visited[i] = True

		if a[i] in visited_a:
			dfs_true(i)
			return

		visited_a.add(a[i])

		for j in edges[i]:
			if not visited[j]:
				dfs(j)

		visited_a.remove(a[i])

	def dfs_true(i):
		visited[i] = True
		result[i] = True

		for j in edges[i]:
			if not visited[j]:
				dfs_true(j)

	setrecursionlimit(10 ** 7)
	dfs(0)

	for i in result:
		print("Yes" if i else "No")


if __name__ == "__main__":
	main()
