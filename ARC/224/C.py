from sys import setrecursionlimit


def solve():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)

	result = [-1] * n

	visited = [False] * n

	def dfs(i, current):
		visited[i] = True
		result[i] = current

		for j in edges[i]:
			if not visited[j]:
				dfs(j, current + 1)

	setrecursionlimit(10 ** 7)
	dfs(0, 0)

	print(*result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
