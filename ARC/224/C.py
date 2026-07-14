from sys import setrecursionlimit


def solve():
	# noinspection DuplicatedCode
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)

	result = [-1] * n

	def dfs(node, current_number):
		result[node] = current_number

		for i in edges[node]:
			if result[i] == -1:
				dfs(i, current_number + 1)

	setrecursionlimit(10 ** 7)
	dfs(0, 0)
	print(*result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
