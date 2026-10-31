from bisect import bisect_right, bisect_left


def main():
	h, w, n, q = [int(i) for i in input().split()]
	pieces_row = []
	pieces_col = []
	for _ in range(n):
		r, c = [int(i) - 1 for i in input().split()]
		pieces_row.append(r)
		pieces_col.append(c)
	pieces_row.sort()
	pieces_col.sort()

	for _ in range(q):
		match [int(i) - 1 for i in input().split()]:
			case 0, u, d:
				left = bisect_left(pieces_row, u)
				right = bisect_right(pieces_row, d) - 1
				if 0 <= left <= right < n:
					print(right - left + 1)
				else:
					print(0)
			case 1, l, r:
				left = bisect_left(pieces_col, l)
				right = bisect_right(pieces_col, r) - 1
				if 0 <= left <= right < n:
					print(right - left + 1)
				else:
					print(0)


if __name__ == "__main__":
	main()
