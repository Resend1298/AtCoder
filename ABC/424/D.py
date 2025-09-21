# TODO: WA

def solve():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	count = [[0] * w for _ in range(h)]
	for i in range(h - 1):
		for j in range(w - 1):
			if s[i][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#':
				count[i][j] += 1
				count[i][j + 1] += 1
				count[i + 1][j] += 1
				count[i + 1][j + 1] += 1

	count_set = [set() for _ in range(5)]
	for i in range(h):
		for j in range(w):
			if count[i][j] > 0:
				count_set[count[i][j]].add((i, j))

	result = 0
	for i in range(4, 0, -1):
		while count_set[i]:
			x, y = count_set[i].pop()
			count[x][y] = 0
			result += 1

			if 0 <= x - 1 < h - 1 and 0 <= y - 1 < w - 1 and count[x - 1][y - 1] > 0 and count[x - 1][y] > 0 and \
					count[x][y - 1] > 0:
				count_set[count[x - 1][y - 1]].discard((x - 1, y - 1))
				count_set[count[x - 1][y]].discard((x - 1, y))
				count_set[count[x][y - 1]].discard((x, y - 1))
				count[x - 1][y - 1] -= 1
				count[x - 1][y] -= 1
				count[x][y - 1] -= 1
				if count[x - 1][y - 1] > 0:
					count_set[count[x - 1][y - 1]].add((x - 1, y - 1))
				if count[x - 1][y] > 0:
					count_set[count[x - 1][y]].add((x - 1, y))
				if count[x][y - 1] > 0:
					count_set[count[x][y - 1]].add((x, y - 1))
			if 0 <= x - 1 < h - 1 and 0 < y + 1 <= w - 1 and count[x - 1][y] > 0 and count[x - 1][y + 1] > 0 and \
					count[x][y + 1] > 0:
				count_set[count[x - 1][y]].discard((x - 1, y))
				count_set[count[x - 1][y + 1]].discard((x - 1, y + 1))
				count_set[count[x][y + 1]].discard((x, y + 1))
				count[x - 1][y] -= 1
				count[x - 1][y + 1] -= 1
				count[x][y + 1] -= 1
				if count[x - 1][y] > 0:
					count_set[count[x - 1][y]].add((x - 1, y))
				if count[x - 1][y + 1] > 0:
					count_set[count[x - 1][y + 1]].add((x - 1, y + 1))
				if count[x][y + 1] > 0:
					count_set[count[x][y + 1]].add((x, y + 1))
			if 0 < x + 1 <= h - 1 and 0 <= y - 1 < w - 1 and count[x][y - 1] > 0 and count[x + 1][y - 1] > 0 and \
					count[x + 1][y] > 0:
				count_set[count[x][y - 1]].discard((x, y - 1))
				count_set[count[x + 1][y - 1]].discard((x + 1, y - 1))
				count_set[count[x + 1][y]].discard((x + 1, y))
				count[x][y - 1] -= 1
				count[x + 1][y - 1] -= 1
				count[x + 1][y] -= 1
				if count[x][y - 1] > 0:
					count_set[count[x][y - 1]].add((x, y - 1))
				if count[x + 1][y - 1] > 0:
					count_set[count[x + 1][y - 1]].add((x + 1, y - 1))
				if count[x + 1][y] > 0:
					count_set[count[x + 1][y]].add((x + 1, y))
			if 0 < x + 1 <= h - 1 and 0 < y + 1 <= w - 1 and count[x][y + 1] > 0 and count[x + 1][y] > 0 and \
					count[x + 1][y + 1] > 0:
				count_set[count[x][y + 1]].discard((x, y + 1))
				count_set[count[x + 1][y]].discard((x + 1, y))
				count_set[count[x + 1][y + 1]].discard((x + 1, y + 1))
				count[x][y + 1] -= 1
				count[x + 1][y] -= 1
				count[x + 1][y + 1] -= 1
				if count[x][y + 1] > 0:
					count_set[count[x][y + 1]].add((x, y + 1))
				if count[x + 1][y] > 0:
					count_set[count[x + 1][y]].add((x + 1, y))
				if count[x + 1][y + 1] > 0:
					count_set[count[x + 1][y + 1]].add((x + 1, y + 1))

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
