def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a.sort()
	result = []

	l = a[-1]
	l_count = a.count(l)
	if (n - l_count) % 2 == 0:
		half_count = (n - l_count) // 2
		for i in range(half_count):
			if a[i] + a[n - l_count - 1 - i] != l:
				break
		else:
			result.append(a[-1])

	if n % 2 == 0:
		half_count = n // 2
		l = a[0] + a[-1]
		for i in range(half_count):
			if a[i] + a[n - 1 - i] != l:
				break
		else:
			result.append(a[0] + a[-1])

	result.sort()
	print(*result)


if __name__ == "__main__":
	main()
