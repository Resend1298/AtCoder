from sortedcontainers import SortedList


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v, c = [int(i) for i in input().split()]
		edges[u].append((v, c))

	sl = SortedList()
	cost = [float("inf")] * n

	sl.add((0, 0))
	cost[0] = 0

	while sl:
		current_cost, current_node = sl.pop(0)

		if current_cost > cost[current_node]:
			continue

		for new_node, edge_cost in edges[current_node]:
			if cost[new_node] > current_cost + edge_cost:
				sl.add((current_cost + edge_cost, new_node))
				cost[new_node] = current_cost + edge_cost

	print(cost[-1])


if __name__ == "__main__":
	main()
