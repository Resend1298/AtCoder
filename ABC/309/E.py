import sys


def main():
	n, m = [int(i) for i in input().split()]

	p = [int(i) - 1 for i in input().split()]
	children = [[] for _ in range(n)]
	for i in range(n - 1):
		children[p[i]].append(i + 1)

	covered_gen = [-1] * n
	for _ in range(m):
		x, y = [int(i) for i in input().split()]
		covered_gen[x - 1] = max(covered_gen[x - 1], y)

	def dfs(i, remaining_gen):
		covered_gen[i] = max(covered_gen[i], remaining_gen)

		for j in children[i]:
			dfs(j, covered_gen[i] - 1)

	sys.setrecursionlimit(10 ** 7)
	dfs(0, -1)

	print([i >= 0 for i in covered_gen].count(True))


if __name__ == "__main__":
	main()
