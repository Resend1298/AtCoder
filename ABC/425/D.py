def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	black_1 = set()
	black_0 = set()
	result = 0

	for i in range(h):
		for j in range(w):
			if s[i][j] == '#':
				result += 1
				continue

			tmp = 0
			for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
				if 0 <= x < h and 0 <= y < w and s[x][y] == '#':
					tmp += 1

			if tmp == 1:
				black_1.add((i, j))
			elif tmp == 0:
				black_0.add((i, j))

	while black_1:
		black_1_new = set()

		for i, j in black_1:
			result += 1
			for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
				if (x, y) in black_0:
					black_0.remove((x, y))
					black_1_new.add((x, y))
				elif (x, y) in black_1_new:
					black_1_new.remove((x, y))

		black_1 = black_1_new

	print(result)


if __name__ == "__main__":
	main()
