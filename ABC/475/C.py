from bisect import bisect_right


def main():
	n, s, l = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	left = []
	for i in range(s - 2, -1, -1):
		if left:
			left.append(left[-1] + a[i])
		else:
			left.append(a[i])

	right = []
	for i in range(s - 1, n - 1):
		if right:
			right.append(right[-1] + a[i])
		else:
			right.append(a[i])

	result = float("-inf")

	if left and right and left[0] > l and right[0] > l:
		print(1)
		exit()
	elif not right and left and left[0] > l:
		print(1)
		exit()
	elif not left and right and right[0] > l:
		print(1)
		exit()

	for left_index in range(len(left)):
		if left[left_index] > l:
			break
		remaining = l - 2 * left[left_index]
		right_index = bisect_right(right, remaining) - 1
		if right_index != -1:
			result = max(result, left_index + 1 + right_index + 1 + 1)
		else:
			result = max(result, left_index + 1 + 1)

	for right_index in range(len(right)):
		if right[right_index] > l:
			break
		remaining = l - 2 * right[right_index]
		left_index = bisect_right(left, remaining) - 1
		if left_index != -1:
			result = max(result, right_index + 1 + left_index + 1 + 1)
		else:
			result = max(result, right_index + 1 + 1)

	print(result)


if __name__ == "__main__":
	main()
