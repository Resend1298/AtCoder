def main():
	h, w = [int(i) for i in input().split()]
	a = [[int(i) for i in input().split()] for _ in range(h)]
	p = [int(i) for i in input().split()]

	result = [[0] * w for _ in range(h)]

	for i in range(h - 1, -1, -1):
		for j in range(w - 1, -1, -1):
			if i < h - 1 and j < w - 1:
				result[i][j] = max(min(result[i + 1][j], result[i][j + 1]) + p[i + j] - a[i][j], 0)
			elif i < h - 1:
				result[i][j] = max(result[i + 1][j] + p[i + j] - a[i][j], 0)
			elif j < w - 1:
				result[i][j] = max(result[i][j + 1] + p[i + j] - a[i][j], 0)
			else:
				result[i][j] = max(p[i + j] - a[i][j], 0)

	print(result[0][0])


if __name__ == "__main__":
	main()
