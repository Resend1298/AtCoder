def main():
	n, k = [int(i) for i in input().split()]
	lr = [[int(i) for i in input().split()] for _ in range(n)]

	lr.sort(key=lambda x: x[1])

	search_l = 0
	search_r = 10 ** 9
	while search_r - search_l != 1:
		mid = (search_l + search_r) // 2

		count = 1
		pre_r = lr[0][1]
		for l, r in lr[1:]:
			if l >= pre_r + mid:
				count += 1
				pre_r = r

		if count >= k:
			search_l = mid
		else:
			search_r = mid

	print(search_l if search_l != 0 else -1)


if __name__ == "__main__":
	main()
