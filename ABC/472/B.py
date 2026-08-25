def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	result = float("inf")
	for i in range(n - 1):
		result = min(result, abs(sum(l[:i + 1]) - sum(l[i + 1:])))

	print(result)


if __name__ == "__main__":
	main()
