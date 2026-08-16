# TODO: review

from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_sl = SortedList(a)
	result = 0
	current_index = 0

	for _ in range(n):
		right_index = a_sl.bisect_right(current_index)
		left_index = right_index - 1
		if right_index != len(a_sl) and left_index != -1:
			if abs(current_index - a_sl[left_index]) <= abs(current_index - a_sl[right_index]):
				result += abs(current_index - a_sl[left_index])
				current_index = a_sl[left_index]
				del a_sl[left_index]
			else:
				result += abs(current_index - a_sl[right_index])
				current_index = a_sl[right_index]
				del a_sl[right_index]
		elif right_index != len(a_sl):
			result += abs(current_index - a_sl[right_index])
			current_index = a_sl[right_index]
			del a_sl[right_index]
		else:
			result += abs(current_index - a_sl[left_index])
			current_index = a_sl[left_index]
			del a_sl[left_index]

	print(result)


if __name__ == "__main__":
	main()
