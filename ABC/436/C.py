def main():
	n, m = [int(i) for i in input().split()]

	placed = set()

	for _ in range(m):
		r, c = [int(i) - 1 for i in input().split()]
		if all(i not in placed for i in [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]):
			placed.update([(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)])

	print(len(placed) // 4)


if __name__ == "__main__":
	main()
