def main():
	h, w = [int(i) for i in input().split()]
	c = [input() for _ in range(h)]

	black_index = [(i, j) for i in range(h) for j in range(w) if c[i][j] == '#']
	black_index_up = min(i for i, _ in black_index)
	black_index_down = max(i for i, _ in black_index)
	black_index_left = min(j for _, j in black_index)
	black_index_right = max(j for _, j in black_index)

	for i in range(black_index_up, black_index_down + 1):
		print(c[i][black_index_left:black_index_right + 1])


if __name__ == "__main__":
	main()
