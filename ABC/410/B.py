def main():
	n, q = [int(i) for i in input().split()]
	x = [int(i) for i in input().split()]

	count = [0] * n
	result = []

	for i in x:
		if i >= 1:
			count[i - 1] += 1
			result.append(i)
		else:
			tmp = count.index(min(count))
			count[tmp] += 1
			result.append(tmp + 1)

	print(*result)


if __name__ == "__main__":
	main()
