# CPython TLE, PyPy AC

def main():
	n = int(input())
	udlr = [[int(i) - 1 for i in input().split()] for _ in range(n)]

	imos = [[0] * 2000 for _ in range(2000)]
	for u, d, l, r in udlr:
		imos[u][l] += 1
		if d + 1 < 2000 and r + 1 < 2000:
			imos[d + 1][r + 1] += 1
		if d + 1 < 2000:
			imos[d + 1][l] -= 1
		if r + 1 < 2000:
			imos[u][r + 1] -= 1
	# noinspection DuplicatedCode
	for i in range(2000):
		for j in range(1, 2000):
			imos[i][j] += imos[i][j - 1]
	for j in range(2000):
		for i in range(1, 2000):
			imos[i][j] += imos[i - 1][j]

	not_covered_by_any = 0
	for i in range(2000):
		for j in range(2000):
			if imos[i][j] == 0:
				not_covered_by_any += 1

	prefix_sum = [[0] * 2000 for _ in range(2000)]
	for i in range(2000):
		for j in range(2000):
			if imos[i][j] == 1:
				prefix_sum[i][j] = 1
	# noinspection DuplicatedCode
	for i in range(2000):
		for j in range(1, 2000):
			prefix_sum[i][j] += prefix_sum[i][j - 1]
	for j in range(2000):
		for i in range(1, 2000):
			prefix_sum[i][j] += prefix_sum[i - 1][j]

	for u, d, l, r in udlr:
		result = not_covered_by_any
		result += prefix_sum[d][r]
		if l - 1 >= 0:
			result -= prefix_sum[d][l - 1]
		if u - 1 >= 0:
			result -= prefix_sum[u - 1][r]
		if u - 1 >= 0 and l - 1 >= 0:
			result += prefix_sum[u - 1][l - 1]
		print(result)


if __name__ == "__main__":
	main()
