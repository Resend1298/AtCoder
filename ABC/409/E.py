import sys


def dfs(i):
	# noinspection PyGlobalUndefined
	global visited, x, result, edge

	visited[i] = True

	for j, w in edge[i]:
		if not visited[j]:
			dfs(j)
			result += w * abs(x[j])
			x[i] += x[j]


def main():
	# noinspection PyGlobalUndefined
	global visited, x, result, edge
	sys.setrecursionlimit(10 ** 7)

	n = int(input())
	x = [int(i) for i in input().split()]
	edge = [[] for _ in range(n)]
	for _ in range(n - 1):
		u, v, w = [int(i) for i in input().split()]
		edge[u - 1].append((v - 1, w))
		edge[v - 1].append((u - 1, w))

	visited = [False] * n
	result = 0

	dfs(0)

	print(result)


if __name__ == "__main__":
	main()
