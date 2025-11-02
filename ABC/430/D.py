# TODO: review

from sortedcontainers import SortedList


def main():
	n = int(input())
	x = [int(i) for i in input().split()]

	result = 0
	location = SortedList([0])

	for i in x:
		if i > location[-1]:
			if len(location) != 1:
				tmp = location[-1] - location[-2]
				if tmp <= i - location[-1]:
					result += i - location[-1]
					location.add(i)
				else:
					result -= tmp
					result += (i - location[-1]) * 2
					location.add(i)
			else:
				result += (i - location[-1]) * 2
				location.add(i)
		else:
			left = location.bisect_left(i) - 1
			right = left + 1
			left_value = location[left]
			right_value = location[right]

			result += min(i - left_value, right_value - i)

			if left != 0:
				left_current_d = min(left_value - location[left - 1], right_value - left_value)
			else:
				left_current_d = right_value - left_value
			if i - left_value < left_current_d:
				result -= left_current_d
				result += i - left_value

			if right != len(location) - 1:
				right_current_d = min(right_value - left_value, location[right + 1] - right_value)
			else:
				right_current_d = right_value - left_value
			if right_value - i < right_current_d:
				result -= right_current_d
				result += right_value - i

			location.add(i)

		print(result)


if __name__ == "__main__":
	main()
