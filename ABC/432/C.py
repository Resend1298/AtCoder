def main():
	n, x, y = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.sort()

	if x * a[-1] > y * a[0]:
		print(-1)
		exit()

	result = a[0]
	for i in a[1:]:
		if (y * (i - a[0])) % (y - x) != 0:
			print(-1)
			exit()
		else:
			result += i - y * (i - a[0]) // (y - x)

	print(result)


if __name__ == "__main__":
	main()
