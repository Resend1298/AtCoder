def main():
	h, w = [int(i) for i in input().split()]

	result = [[0] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= x < h and 0 <= y < w:
					result[i][j] += 1

	for i in result:
		print(*i)


if __name__ == "__main__":
	main()
