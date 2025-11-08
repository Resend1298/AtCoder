from sortedcontainers import SortedList


def main():
	n, m, k = [int(i) for i in input().split()]
	h = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	h.sort()
	b = SortedList(b)
	result = 0

	for i in h:
		body_index = b.bisect_left(i)
		if body_index == len(b):
			break
		else:
			result += 1
			b.pop(body_index)

	if result >= k:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
