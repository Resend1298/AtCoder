# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)
		edges[b].append(a)

	result = []
	for i in range(n):
		possible = n - 1 - len(edges[i])
		if possible >= 3:
			result.append(possible * (possible - 1) * (possible - 2) // 6)
		else:
			result.append(0)

	print(*result)


if __name__ == "__main__":
	main()
