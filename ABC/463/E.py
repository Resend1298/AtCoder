from sortedcontainers import SortedList


def main():
	"""
	Add n virtual nodes to represent the warp gates, where node[i+n] represents the warp gate at node i.
	Add edges from real nodes to virtual nodes, from virtual nodes to real nodes, and between virtual nodes to represent the warp paths.
	Edges from real nodes to virtual nodes cost x[i]+y, edges from virtual nodes to real nodes cost x[i], and edges between virtual nodes cost 0.
	"""

	n, m, y = [int(i) for i in input().split()]
	edges = [[] for _ in range(n * 2)]
	# noinspection DuplicatedCode
	for _ in range(m):
		# noinspection DuplicatedCode
		u, v, t = [int(i) for i in input().split()]
		edges[u - 1].append((v - 1, t))
		edges[v - 1].append((u - 1, t))
	x = [int(i) for i in input().split()]

	# Add virtual edges
	for i in range(n):
		edges[i].append((i + n, x[i] + y))
		edges[i + n].append((i, x[i]))
	for i in range(n, n * 2 - 1):
		edges[i].append((i + 1, 0))
		edges[i + 1].append((i, 0))

	sl = SortedList()
	cost = [float("inf")] * (n * 2)
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

	print(*cost[1:n])


if __name__ == "__main__":
	main()
