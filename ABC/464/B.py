def main():
	h, w = [int(i) for i in input().split()]
	c = [input() for _ in range(h)]

	black = [(i, j) for i in range(h) for j in range(w) if c[i][j] == '#']
	up = min(i for i, _ in black)
	down = max(i for i, _ in black)
	left = min(j for _, j in black)
	right = max(j for _, j in black)

	for i in c[up:down + 1]:
		print(i[left:right + 1])


if __name__ == "__main__":
	main()
