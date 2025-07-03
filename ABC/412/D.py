from itertools import combinations


def main():
	n, m = [int(i) for i in input().split()]
	edges = [set() for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[min(a, b)].add(max(a, b))

	result = m + n
	new_edges = [set() for _ in range(n)]
	degrees = [0] * n

	def dfs(current_vertex):
		if current_vertex == n - 1:
			if degrees[current_vertex] == 2:
				tmp_result = 0
				for i in range(n):
					tmp_result += len(new_edges[i] - edges[i])
					tmp_result += len(edges[i] - new_edges[i])
				nonlocal result
				result = min(result, tmp_result)
			return

		match degrees[current_vertex]:
			case 2:
				dfs(current_vertex + 1)
			case 1:
				for i in range(current_vertex + 1, n):
					if degrees[i] < 2:
						new_edges[current_vertex].add(i)
						degrees[i] += 1
						dfs(current_vertex + 1)
						new_edges[current_vertex].remove(i)
						degrees[i] -= 1
			case 0:
				for i, j in combinations(range(current_vertex + 1, n), 2):
					if degrees[i] < 2 and degrees[j] < 2:
						new_edges[current_vertex].add(i)
						new_edges[current_vertex].add(j)
						degrees[i] += 1
						degrees[j] += 1
						dfs(current_vertex + 1)
						new_edges[current_vertex].remove(i)
						new_edges[current_vertex].remove(j)
						degrees[i] -= 1
						degrees[j] -= 1

	dfs(0)

	print(result)


if __name__ == "__main__":
	main()
