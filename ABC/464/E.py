def main():
	h, w, q = [int(i) for i in input().split()]
	rcx = [input().split() for _ in range(q)]

	grid = [[' '] * w for _ in range(h)]

	for r, c, x in rcx[::-1]:
		r, c = int(r) - 1, int(c) - 1
		if grid[r][c] != ' ':
			continue
		for i in range(r - 1, -1, -1):
			if grid[i][c] != ' ':
				up = i + 1
				break
		else:
			up = 0
		for i in range(r, up - 1, -1):
			for j in range(c, -1, -1):
				if grid[i][j] != ' ':
					break
				grid[i][j] = x

	for i in range(h):
		for j in range(w):
			if grid[i][j] == ' ':
				grid[i][j] = 'A'

	for i in grid:
		print(''.join(i))


if __name__ == "__main__":
	main()
