from collections import deque


def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	result = float("-inf")
	q: deque[tuple[float, int, int]] = deque()
	q.append((0.5, 0, 0))

	while q:
		current_index, next_move, current_result = q.popleft()

		if next_move == n:
			result = max(result, current_result)
			continue

		for new_index in [current_index + l[next_move], current_index - l[next_move]]:
			if current_index * new_index < 0:
				q.append((new_index, next_move + 1, current_result + 1))
			else:
				q.append((new_index, next_move + 1, current_result))

	print(result)


if __name__ == "__main__":
	main()
