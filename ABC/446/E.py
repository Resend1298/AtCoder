def main():
	m, a, b = [int(i) for i in input().split()]

	result = 0
	cache = {}
	cache_result = {}

	for x in range(m):
		for y in range(m):
			if x == 0 or y == 0:
				cache_result[(x, y)] = False
				cache[(x, y)] = (x, y)
				continue

			n_2 = x
			n_1 = y
			while True:
				new = (a * n_1 + b * n_2) % m
				n_2 = n_1
				n_1 = new

				if new == 0:
					cache_result[(x, y)] = False
					cache[(n_2, n_1)] = (x, y)
					break

				if (n_2, n_1) in cache:
					if cache[(n_2, n_1)] in cache_result:
						if cache_result[cache[(n_2, n_1)]]:
							result += 1
							cache_result[(x, y)] = True
						else:
							cache_result[(x, y)] = False
					else:
						result += 1
						cache_result[(x, y)] = True
					break

				cache[(n_2, n_1)] = (x, y)

	print(result)


if __name__ == "__main__":
	main()
