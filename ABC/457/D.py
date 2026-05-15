def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	l = min(a)
	r = min(a) + k * (a.index(min(a)) + 1) + 1
	while r - l != 1:
		mid = (l + r) // 2
		if sum((mid - a[i] + i) // (i + 1) for i in range(n) if a[i] < mid) <= k:
			l = mid
		else:
			r = mid

	print(l)


if __name__ == "__main__":
	main()
