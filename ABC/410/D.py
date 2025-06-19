import sys


def main():
	sys.setrecursionlimit(10 ** 7)

	n, m = [int(i) for i in input().split()]
	edge = [[] for _ in range(n)]
	for _ in range(m):
		a, b, w = [int(i) for i in input().split()]
		edge[a - 1].append((b - 1, w))

	visited = [[False] * 1024 for _ in range(n)]

	def dfs(i, j):
		visited[i][j] = True

		for k, l in edge[i]:
			if not visited[k][j ^ l]:
				dfs(k, j ^ l)

	dfs(0, 0)

	for i in range(1024):
		if visited[n - 1][i]:
			print(i)
			exit()
	else:
		print(-1)


if __name__ == "__main__":
	main()
