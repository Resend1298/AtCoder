from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	remaining = SortedList(a)
	result = 0
	current_index = 0

	for _ in range(n):
		right = remaining.bisect_right(current_index)
		left = right - 1

		if right != len(remaining) and left != -1:
			right = remaining[right]
			left = remaining[left]
			next_index = right if right - current_index < current_index - left else left
		elif right != len(remaining):
			next_index = remaining[right]
		else:
			next_index = remaining[left]

		result += abs(next_index - current_index)
		current_index = next_index
		remaining.remove(next_index)

	print(result)


if __name__ == "__main__":
	main()
