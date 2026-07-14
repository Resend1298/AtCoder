def main():
	t, x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = []
	for i, j in enumerate(a):
		if i == 0 or abs(j - result[-1][1]) >= x:
			result.append((i, j))

	for i, j in result:
		print(i, j)


if __name__ == "__main__":
	main()
