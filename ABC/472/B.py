def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	result = float("inf")
	for i in range(1, n):
		result = min(result, abs(sum(l[:i]) - sum(l[i:])))

	print(result)


if __name__ == "__main__":
	main()
