def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	l = -1
	r = n
	while r - l != 1:
		mid = (l + r) // 2
		if a[mid] >= k:
			r = mid
		else:
			l = mid

	if r != n:
		print(r)
	else:
		print(-1)


if __name__ == "__main__":
	main()
