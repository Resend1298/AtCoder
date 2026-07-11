def main():
	n, m = [int(i) for i in input().split()]
	cs = [[int(i) for i in input().split()] for _ in range(n)]

	biggest_by_color = [-1] * m
	for c, s in cs:
		biggest_by_color[c - 1] = max(biggest_by_color[c - 1], s)

	print(*biggest_by_color)


if __name__ == "__main__":
	main()
