def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) - 1 for i in input().split()]

	black = [False] * n
	result = 0

	for i in a:
		if not black[i]:
			if n == 1 or (i != 0 and i != n - 1 and not black[i - 1] and not black[i + 1]) or (
					i == 0 and not black[i + 1]) or (
					i == n - 1 and not black[i - 1]):
				result += 1
			elif i != 0 and i != n - 1 and black[i - 1] and black[i + 1]:
				result -= 1
			black[i] = True
		else:
			if n == 1 or (i != 0 and i != n - 1 and not black[i - 1] and not black[i + 1]) or (
					i == 0 and not black[i + 1]) or (
					i == n - 1 and not black[i - 1]):
				result -= 1
			elif i != 0 and i != n - 1 and black[i - 1] and black[i + 1]:
				result += 1
			black[i] = False
		print(result)


if __name__ == "__main__":
	main()
