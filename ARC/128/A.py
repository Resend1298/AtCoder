def main():
	# exchange to silver at the highest point
	# exchange to gold at the lowest point

	n = int(input())
	a = [int(i) for i in input().split()]

	result = [0] * n

	highest = 0
	while highest < n - 1:
		while highest + 1 < n and a[highest + 1] >= a[highest]:
			highest += 1
		if highest == n - 1:
			break

		lowest = highest + 1
		while lowest + 1 < n and a[lowest + 1] <= a[lowest]:
			lowest += 1

		result[highest] = 1
		result[lowest] = 1
		highest = lowest + 1

	print(*result)


if __name__ == "__main__":
	main()
