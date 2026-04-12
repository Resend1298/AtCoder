# TODO: review

def main():
	t, x = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = [(0, a[0])]
	for i in range(1, t + 1):
		if abs(a[i] - result[-1][1]) >= x:
			result.append((i, a[i]))

	for i, j in result:
		print(i, j)


if __name__ == "__main__":
	main()
