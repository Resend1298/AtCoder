def main():
	l, r, d, u = [int(i) for i in input().split()]

	result = 0
	for y in range(d, u + 1):
		y = abs(y)

		if y % 2 == 0:
			result += min(y, r) - max(-y, l) + 1 if min(y, r) >= max(-y, l) else 0

		if y % 2 == 1:
			y -= 1
		left = max(y + 2, l)
		right = r
		if left <= right:
			result += (right - left + 1) // 2 if not (left % 2 == 0 and right % 2 == 0) else (right - left + 1) // 2 + 1
		left = l
		right = min(-y - 2, r)
		if left <= right:
			result += (right - left + 1) // 2 if not (left % 2 == 0 and right % 2 == 0) else (right - left + 1) // 2 + 1

	print(result)


if __name__ == "__main__":
	main()
