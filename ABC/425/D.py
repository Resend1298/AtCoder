def main():
	h, w = [int(i) for i in input().split()]
	s = [list(input()) for _ in range(h)]

	black_0 = set()
	black_1 = set()

	for i in range(h):
		for j in range(w):
			if s[i][j] == '.':
				# noinspection DuplicatedCode
				tmp = 0
				for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
					if 0 <= x < h and 0 <= y < w and s[x][y] == '#':
						tmp += 1

				if tmp == 0:
					black_0.add((i, j))
				elif tmp == 1:
					black_1.add((i, j))

	while black_1:
		new_black_1 = set()

		for i, j in black_1:
			s[i][j] = '#'
			for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
				if (x, y) in black_0:
					black_0.remove((x, y))
					new_black_1.add((x, y))
				elif (x, y) in new_black_1:
					new_black_1.remove((x, y))

		black_1 = new_black_1

	print(sum(i.count('#') for i in s))


if __name__ == "__main__":
	main()
