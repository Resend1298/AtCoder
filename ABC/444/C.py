def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a.sort()
	result = []

	# all sticks broke
	if n % 2 == 0 and all(a[i] + a[n - 1 - i] == a[0] + a[-1] for i in range(n // 2)):
		result.append(a[0] + a[-1])

	# at least one stick remains
	l = a[-1]
	l_count = a.count(l)
	if (n - l_count) % 2 == 0 and all(a[i] + a[n - l_count - 1 - i] == l for i in range((n - l_count) // 2)):
		result.append(l)

	result.sort()
	print(*result)


if __name__ == "__main__":
	main()
