def main():
	n, q = [int(i) for i in input().split()]

	imos_plus = [[] for _ in range(n)]
	imos_minus = [[] for _ in range(n)]

	for _ in range(q):
		l, r, x = [int(i) for i in input().split()]
		imos_plus[l - 1].append(x)
		if r < n:
			imos_minus[r].append(x)

	current = {}
	result = []

	for i in range(n):
		for x in imos_plus[i]:
			if x in current:
				current[x] += 1
			else:
				current[x] = 1
		for x in imos_minus[i]:
			current[x] -= 1
			if current[x] == 0:
				del current[x]

		result.append(len(current))

	print(*result)


if __name__ == "__main__":
	main()
