def main():
	n = int(input())
	x, y = [], []
	for _ in range(n):
		r, c = [int(i) - 1 for i in input().split()]
		x.append(r)
		y.append(c)

	center_x = (min(x) + max(x)) // 2
	center_y = (min(y) + max(y)) // 2
	result = max(abs(min(x) - center_x), abs(max(x) - center_x), abs(min(y) - center_y), abs(max(y) - center_y))

	print(result)


if __name__ == "__main__":
	main()
