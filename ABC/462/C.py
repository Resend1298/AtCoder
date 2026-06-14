def main():
	n = int(input())
	xy = [[int(i) for i in input().split()] for _ in range(n)]

	xy.sort(key=lambda x: x[0])
	pre_min_y = float("inf")
	result = 0

	for _, y in xy:
		if y < pre_min_y:
			pre_min_y = y
			result += 1

	print(result)


if __name__ == "__main__":
	main()
