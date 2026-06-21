# TODO: review

from sortedcontainers import SortedKeyList


def main():
	n, m, y = [int(i) for i in input().split()]
	edges = [[] for _ in range(n * 2)]
	for _ in range(m):
		u, v, t = [int(i) for i in input().split()]
		edges[u - 1].append((v - 1, t))
		edges[v - 1].append((u - 1, t))
	x = [int(i) for i in input().split()]
	for i in range(n, n * 2):
		edges[i].append((i - n, x[i - n]))
		edges[i - n].append((i, x[i - n] + y))
		if i != n * 2 - 1:
			edges[i].append((i + 1, 0))
			edges[i + 1].append((i, 0))

	q = SortedKeyList([(0, 0)], key=lambda x: (x[1], x[0]))
	cost = [float("inf")] * (n * 2)
	cost[0] = 0
	visited = set()

	while q:
		current_location, current_cost = q.pop(0)
		if current_location in visited:
			continue
		visited.add(current_location)
		for next_location, next_cost in edges[current_location]:
			if cost[next_location] > cost[current_location] + next_cost:
				cost[next_location] = cost[current_location] + next_cost
				q.add((next_location, cost[next_location]))

	print(*cost[1:n])


if __name__ == "__main__":
	main()
