# CPython TLE, PyPy AC

from sortedcontainers import SortedList


def diff_bigger_equal_d(sl, value, d):
	index = sl.bisect_left(value)
	if index - 1 >= 0 and value - sl[index - 1] < d:
		return False
	if index < len(sl) and sl[index] - value < d:
		return False
	return True


def main():
	n, d = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	r = 0
	result = 0
	current = SortedList([a[0]])

	for l in range(n):
		while r + 1 < n and diff_bigger_equal_d(current, a[r + 1], d):
			r += 1
			current.add(a[r])

		result += r - l + 1

		current.remove(a[l])

		if l == r and r + 1 < n:
			r += 1
			current.add(a[r])

	print(result)


if __name__ == "__main__":
	main()
