from collections import Counter
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
	visited_a = Counter()
	result = [True] * n

	def dfs(i):
		visited[i] = True
		visited_a[a[i]] += 1
		if visited_a[a[i]] >= 2:
			dfs_false(i)

		for j in edges[i]:
			if not visited[j]:
				dfs(j)

		visited_a[a[i]] -= 1

	def dfs_false(i):
		visited[i] = True
		result[i] = False
		for j in edges[i]:
			if not visited[j]:
				dfs_false(j)

	setrecursionlimit(10 ** 7)
	dfs(0)

	for i in result:
		print("No" if i else "Yes")


if __name__ == "__main__":
	main()
