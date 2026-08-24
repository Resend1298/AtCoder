# TODO: review

from sys import setrecursionlimit


def solve():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)
		edges[b].append(a)

	visited = [-1] * n
	result = []
	found = False
	target = -1
	target_found = False

	def dfs(node, step):
		nonlocal found
		nonlocal target
		nonlocal target_found

		visited[node] = step

		for i in edges[node]:
			if visited[i] == -1:
				dfs(i, step + 1)

				if found:
					if not target_found:
						result.append(node + 1)
						if node + 1 == target:
							target_found = True
					return
			elif step - visited[i] != 1 and (step + 1 - visited[i]) % 2 == 1:
				target = i + 1
				result.append(node + 1)
				found = True
				return

	setrecursionlimit(10 ** 7)
	dfs(0, 1)

	if not found:
		print(-1)
	else:
		print(len(result))
		print(*result)


def main():
	t = int(input())

	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
