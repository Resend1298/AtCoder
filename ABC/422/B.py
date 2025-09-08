# TODO: review

def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	for i in range(h):
		for j in range(w):
			if s[i][j] == '.':
				continue

			count = 0
			for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
				if 0 <= x < h and 0 <= y < w and s[x][y] == '#':
					count += 1

			if count != 2 and count != 4:
				print("No")
				exit()

	print("Yes")


if __name__ == "__main__":
	main()
