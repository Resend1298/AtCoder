def main():
	m, a, b = [int(i) for i in input().split()]

	result = 0
	cache_satisfied = set()
	cache_not_satisfied = set()

	for x in range(1, m):
		for y in range(1, m):
			if (x, y) in cache_satisfied:
				result += 1
				continue
			if (x, y) in cache_not_satisfied:
				continue

			n_2 = x
			n_1 = y
			encountered = {(n_2, n_1)}

			while True:
				n_2, n_1 = n_1, (a * n_1 + b * n_2) % m

				if (n_2, n_1) in cache_satisfied:
					result += 1
					cache_satisfied |= encountered
					break
				if (n_2, n_1) in cache_not_satisfied:
					cache_not_satisfied |= encountered
					break

				if n_1 == 0:
					cache_not_satisfied |= encountered
					break
				if (n_2, n_1) in encountered:
					result += 1
					cache_satisfied |= encountered
					break

				encountered.add((n_2, n_1))

	print(result)


if __name__ == "__main__":
	main()
