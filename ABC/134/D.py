def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	result = [-1] * n

	for i in range(n - 1, -1, -1):
		tmp = 0
		for j in range(2 * (i + 1) - 1, n, i + 1):
			tmp ^= result[j]
		result[i] = tmp ^ a[i]

	print(result.count(1))
	print(*[i + 1 for i in range(n) if result[i] == 1])


if __name__ == "__main__":
	main()
