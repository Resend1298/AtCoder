def main():
	n, m = [int(i) for i in input().split()]
	s = [int(i) for i in list(input())]
	t = [int(i) for i in list(input())]

	result = float("inf")

	for i in range(n - m + 1):
		tmp = 0
		for j in range(m):
			if s[i + j] > t[j]:
				tmp += s[i + j] - t[j]
			elif s[i + j] < t[j]:
				tmp += 10 - t[j] + s[i + j]
		result = min(result, tmp)

	print(result)


if __name__ == "__main__":
	main()
