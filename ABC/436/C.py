def main():
	n, m = [int(i) for i in input().split()]

	blocks = set()
	result = 0

	for _ in range(m):
		r, c = [int(i) - 1 for i in input().split()]
		if (r, c) not in blocks and (r + 1, c) not in blocks and (r, c + 1) not in blocks and (r + 1,
		                                                                                       c + 1) not in blocks:
			blocks.add((r, c))
			blocks.add((r + 1, c))
			blocks.add((r, c + 1))
			blocks.add((r + 1, c + 1))
			result += 1

	print(result)


if __name__ == "__main__":
	main()
