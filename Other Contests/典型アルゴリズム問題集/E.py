def main():
	n, m = [int(i) for i in input().split()]
	edges: list[list[tuple[int, int]]] = [[] for _ in range(n)]
	for _ in range(m):
		u, v, c = [int(i) for i in input().split()]
		edges[u].append((v, c))

	cost = [[float("inf")] * n for _ in range(n)]
	for i in range(n):
		cost[i][i] = 0
	for i in range(n):
		for j, edge_cost in edges[i]:
			cost[i][j] = min(cost[i][j], edge_cost)

	for k in range(n):
		for i in range(n):
			for j in range(n):
				cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

	print(sum(sum(i) for i in cost))


if __name__ == "__main__":
	main()
