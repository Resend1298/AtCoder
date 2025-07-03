from sortedcontainers import SortedSet


def main():
	t = int(input())

	for _ in range(t):
		_ = int(input())
		s = [int(i) for i in input().split()]

		current = s.pop(0)
		end = s.pop()
		s = SortedSet(s)

		for result in range(len(s)):
			if end <= current * 2:
				print(result + 2)
				break

			next_index = s.bisect_right(current * 2) - 1
			if next_index == -1:
				print(-1)
				break
			current = s[next_index]
		else:
			if end <= current * 2:
				print(len(s) + 2)
			else:
				print(-1)


if __name__ == "__main__":
	main()
