def main():
	n, m = [int(i) for i in input().split()]
	# noinspection DuplicatedCode
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)
		edges[b].append(a)

	result = []

	for i in range(n):
		peer_count = n - 1 - len(edges[i])
		result.append(peer_count * (peer_count - 1) * (peer_count - 2) // 6)

	print(*result)


if __name__ == "__main__":
	main()
