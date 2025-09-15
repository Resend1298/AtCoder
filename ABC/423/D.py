# TODO: review

from collections import deque

from sortedcontainers import SortedKeyList


def main():
	n, k = [int(i) for i in input().split()]
	abc = [[j] + [int(i) for i in input().split()] for j in range(n)]

	waiting = deque(abc)
	eating = SortedKeyList(key=lambda x: x[0])
	enter_time = [0] * n
	remaining_seat = k

	while waiting:
		if remaining_seat >= waiting[0][3]:
			current_time = max(waiting[0][1], enter_time[waiting[0][0] - 1])
			enter_time[waiting[0][0]] = current_time
			remaining_seat -= waiting[0][3]
			eating.add((current_time + waiting[0][2], waiting[0][3]))
			waiting.popleft()
		else:
			while remaining_seat < waiting[0][3]:
				finish_time, seat = eating.pop(0)
				remaining_seat += seat
			enter_time[waiting[0][0]] = max(finish_time, waiting[0][1])
			remaining_seat -= waiting[0][3]
			eating.add((enter_time[waiting[0][0]] + waiting[0][2], waiting[0][3]))
			waiting.popleft()

	for i in enter_time:
		print(i)


if __name__ == "__main__":
	main()
