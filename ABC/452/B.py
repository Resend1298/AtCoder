def main():
	h, w = [int(i) for i in input().split()]

	grid = [['.'] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			if i == 0 or i == h - 1 or j == 0 or j == w - 1:
				grid[i][j] = '#'

	for i in grid:
		print(''.join(i))


if __name__ == "__main__":
	main()
