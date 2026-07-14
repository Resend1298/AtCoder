def main():
	r, b = [int(i) for i in input().split()]
	x, y = [int(i) for i in input().split()]

	left = -1
	right = r + b + 1
	while right - left != 1:
		mid = (left + right) // 2
		if ((y * mid - b + y - 2) // (y - 1) <= (r - mid) // (x - 1)
				and (r - mid) // (x - 1) >= 0
				and (y * mid - b + y - 2) // (y - 1) <= mid):
			left = mid
		else:
			right = mid

	print(left)


if __name__ == "__main__":
	main()
