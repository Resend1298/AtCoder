# TODO: review

from bisect import bisect_right
from math import ceil


def main():
	n, m, k = [int(i) for i in input().split()]
	x, y = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	a.sort()
	b.sort()

	a_sum = [a[0]]
	for i in a[1:]:
		a_sum.append(a_sum[-1] + i)

	start_sum = x + k * y
	a_sum_index = bisect_right(a_sum, start_sum) - 1
	if a_sum_index != -1:
		result = a_sum_index + 1
	else:
		result = 0

	for b_index in range(m):
		tmp = ceil(b[b_index] / k)
		if y < tmp:
			break

		x += k * tmp - b[b_index]
		y -= tmp

		a_sum_index = bisect_right(a_sum, x + k * y) - 1
		result = max(result, b_index + 1 + a_sum_index + 1)

	print(result)


if __name__ == "__main__":
	main()
