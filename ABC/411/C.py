def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) - 1 for i in input().split()]

	black = [False] * n
	result = 0

	for i in a:
		if not black[i]:
			# noinspection DuplicatedCode
			if ((0 < i < n - 1 and not black[i - 1] and not black[i + 1])
					or n == 1
					or (i == 0 and not black[i + 1]) or (i == n - 1 and not black[i - 1])):
				result += 1
			elif 0 < i < n - 1 and black[i - 1] and black[i + 1]:
				result -= 1
			black[i] = True
		else:
			# noinspection DuplicatedCode
			if ((0 < i < n - 1 and not black[i - 1] and not black[i + 1])
					or n == 1
					or (i == 0 and not black[i + 1]) or (i == n - 1 and not black[i - 1])):
				result -= 1
			elif 0 < i < n - 1 and black[i - 1] and black[i + 1]:
				result += 1
			black[i] = False

		print(result)


if __name__ == "__main__":
	main()
