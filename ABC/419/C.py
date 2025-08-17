# TODO: review

def main():
	n = int(input())
	min_x, min_y, max_x, max_y = float("inf"), float("inf"), float("-inf"), float("-inf")
	rc = []
	for _ in range(n):
		r, c = [int(i) - 1 for i in input().split()]
		rc.append((r, c))
		min_x = min(min_x, r)
		min_y = min(min_y, c)
		max_x = max(max_x, r)
		max_y = max(max_y, c)

	center_x = (min_x + max_x) // 2
	center_y = (min_y + max_y) // 2

	result = float("-inf")
	for r, c in rc:
		result = max(result, max(abs(r - center_x), abs(c - center_y)))

	print(result)


if __name__ == "__main__":
	main()
