# CPython TLE, PyPy AC

def main():
	h, w, k = [int(i) for i in input().split()]
	s = [[int(i) for i in list(input())] for _ in range(h)]

	result = 0

	col_prefix_sum = [[0] for _ in range(w)]
	for i in range(w):
		for j in range(h):
			col_prefix_sum[i].append(col_prefix_sum[i][-1] + s[j][i])

	for up in range(h):
		for down in range(up, h):
			r = 0
			r_max = 0
			current = col_prefix_sum[0][down + 1] - col_prefix_sum[0][up]

			for l in range(w):
				while r + 1 < w and current < k:
					r += 1
					current += col_prefix_sum[r][down + 1] - col_prefix_sum[r][up]
				if r == w - 1 and current < k:
					break

				if current == k:
					r_max = max(r_max, r)
					while r_max + 1 < w and col_prefix_sum[r_max + 1][down + 1] - col_prefix_sum[r_max + 1][up] == 0:
						r_max += 1
					result += r_max - r + 1

				current -= col_prefix_sum[l][down + 1] - col_prefix_sum[l][up]

				if l == r and r + 1 < w:
					r += 1
					current += col_prefix_sum[r][down + 1] - col_prefix_sum[r][up]

	print(result)


if __name__ == "__main__":
	main()
