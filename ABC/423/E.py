# TODO: TLE

def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	for _ in range(q):
		l, r = [int(i) - 1 for i in input().split()]

		result = 0
		for i in range(l, r + 1):
			result += a[i] * (i - l + 1) * (r + 1 - i)

		print(result)


if __name__ == "__main__":
	main()
