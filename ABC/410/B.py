def main():
	n, q = [int(i) for i in input().split()]
	x = [int(i) for i in input().split()]

	count = [0] * n
	result = []

	for i in x:
		if i >= 1:
			result.append(i)
			count[i - 1] += 1
		else:
			min_count = float("inf")
			min_index = 0
			for j in range(n):
				if count[j] < min_count:
					min_count = count[j]
					min_index = j
			result.append(min_index + 1)
			count[min_index] += 1

	print(*result)


if __name__ == "__main__":
	main()
