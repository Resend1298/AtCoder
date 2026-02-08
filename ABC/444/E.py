# TODO: review

from sortedcontainers import SortedList


def main():
	n, d = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = 0
	r = 0
	current_min = a[0]
	current_max = a[0]
	current = SortedList([a[0]])

	for l in range(n):
		while r + 1 < n and (a[r + 1] - current_max >= d or current_min - a[r + 1] >= d or current[
			current.bisect_left(a[r + 1]) - 1] + d <= a[r + 1] <= current[current.bisect_left(a[r + 1])] - d):
			r += 1
			current_min = min(current_min, a[r])
			current_max = max(current_max, a[r])
			current.add(a[r])

		result += r - l + 1

		current.remove(a[l])
		current_min = current[0] if current else float("inf")
		current_max = current[-1] if current else float("-inf")

		if l == r and r + 1 < n:
			r += 1
			current_min = min(current_min, a[r])
			current_max = max(current_max, a[r])
			current.add(a[r])

	print(result)


if __name__ == "__main__":
	main()
