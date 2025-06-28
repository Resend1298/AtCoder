from sortedcontainers import SortedList


def main():
	t = int(input())

	for _ in range(t):
		n = int(input())
		s = [int(i) for i in input().split()]

		left = s.pop(0)
		right = s.pop(-1)

		if right <= 2 * left:
			print(2)
			continue

		s = SortedList(s)

		current = left
		for i in range(1, n - 1):
			next_index = s.bisect_right(2 * current) - 1
			if next_index < 0 or next_index >= len(s):
				print(-1)
				break
			current = s[next_index]
			if right <= 2 * current:
				print(i + 2)
				break
		else:
			print(-1)


if __name__ == "__main__":
	main()
