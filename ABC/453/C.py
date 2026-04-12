# TODO: review

from collections import deque


def main():
	n = int(input())
	l = [int(i) for i in input().split()]

	available = [sum(l)]
	for i in l:
		available.append(available[-1] - i)

	q = deque()
	q.append((0.5, 0, 0))
	result = float("-inf")

	while q:
		current, next_move, current_result = q.popleft()

		if next_move == n:
			result = max(result, current_result)
			continue

		if abs(current) > available[next_move]:
			result = max(result, current_result)
			continue

		if n - next_move <= result - current_result:
			result = max(result, current_result)
			continue

		next_current = current + l[next_move]
		if current * next_current < 0:
			q.append((next_current, next_move + 1, current_result + 1))
		else:
			q.append((next_current, next_move + 1, current_result))
		next_current = current - l[next_move]
		if current * next_current < 0:
			q.append((next_current, next_move + 1, current_result + 1))
		else:
			q.append((next_current, next_move + 1, current_result))

	print(result)


if __name__ == "__main__":
	main()
