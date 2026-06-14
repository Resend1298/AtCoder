from math import comb


def main():
	n, d = [int(i) for i in input().split()]
	st = [[int(i) for i in input().split()] for _ in range(n)]

	st = [(s, t - d) for s, t in st if t - s >= d]
	if not st:
		print(0)
		exit()
	min_s = min(s for s, _ in st)
	st = [(s - min_s, t - min_s) for s, t in st]
	max_t = max(t for _, t in st)

	imos = [0] * (max_t + 2)
	for s, t in st:
		imos[s] += 1
		imos[t + 1] -= 1

	result = 0
	current = 0
	for i in imos:
		current += i
		if current >= 2:
			result += comb(current, 2)

	print(result)


if __name__ == "__main__":
	main()
