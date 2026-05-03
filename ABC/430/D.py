# CPython TLE, PyPy AC

from sortedcontainers import SortedList


def main():
	_ = int(input())
	x = [int(i) for i in input().split()]

	first_person = x.pop(0)
	location = SortedList([0, first_person])
	result = first_person * 2
	print(result)

	for i in x:
		if i > location[-1]:
			# will be placed at the right end
			# therefore, only the d_rightest might change

			current_d = location[-1] - location[-2]
			new_d = i - location[-1]
			if new_d < current_d:
				result -= current_d
				result += new_d

			result += i - location[-1]
		else:
			# will be placed between two existing locations
			# therefore, both d_left and d_right might change

			left = location.bisect_left(i) - 1
			right = left + 1

			current_d = min(location[left] - location[left - 1], location[right] - location[left]) if left > 0 else \
				location[right] - location[left]
			new_d = i - location[left]
			if new_d < current_d:
				result -= current_d
				result += new_d

			current_d = min(location[right + 1] - location[right], location[right] - location[left]) if right < len(
				location) - 1 else location[right] - location[left]
			new_d = location[right] - i
			if new_d < current_d:
				result -= current_d
				result += new_d

			result += min(location[right] - i, i - location[left])

		location.add(i)
		print(result)


if __name__ == "__main__":
	main()
