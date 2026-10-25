# TODO: review

from sortedcontainers import SortedList


def main():
	n, m, s, t = [int(i) for i in input().split()]
	s -= 1
	t -= 1
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append([b, 1])

	for i in edges:
		if i:
			i.sort(key=lambda x: x[0])
			i[0][1] = 0

	sl = SortedList()
	cost = [float("inf")] * n

	sl.add((0, s))
	cost[s] = 0

	while sl:
		current_cost, current_node = sl.pop(0)

		if current_cost > cost[current_node]:
			continue

		for new_node, edge_cost in edges[current_node]:
			if cost[new_node] > current_cost + edge_cost:
				sl.add((current_cost + edge_cost, new_node))
				cost[new_node] = current_cost + edge_cost

	if cost[t] != float("inf"):
		print(cost[t])
	else:
		print(-1)


if __name__ == "__main__":
	main()
