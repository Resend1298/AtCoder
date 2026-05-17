# TODO: review

def main():
	h, w = [int(i) for i in input().split()]

	result = [[0] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			for new_x, new_y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
				if 0 <= new_x < h and 0 <= new_y < w:
					result[i][j] += 1

	for i in result:
		print(*i)


if __name__ == "__main__":
	main()
