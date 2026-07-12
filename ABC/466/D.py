# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	rc = [[int(i) - 1 for i in input().split()] for _ in range(m)]

	locked_rows = [False] * n
	locked_cols = [False] * n
	result = 0

	for r, c in rc[::-1]:
		if not locked_rows[r] and not locked_cols[c]:
			result += 1
		locked_rows[r] = True
		locked_cols[c] = True

	print(result)


if __name__ == "__main__":
	main()
