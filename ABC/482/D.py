def main():
	n = int(input())
	x = [int(i) for i in input().split()]

	for i in range(n):
		if i == 0 or i == n - 1:
			print((x[-1] - x[0]) // 2)
			continue

		result = float("inf")
		tmp_left = 0
		tmp_right = 0

		# left
		tmp_left += (x[i] - x[i - 1]) // 2
		current_index = (x[i] + x[i - 1]) // 2
		if i - 2 >= 0 and i + 1 < n:
			tmp_left += max(max(0, current_index - x[0] - tmp_left), max(0, x[-1] - tmp_left - current_index)) // 2
		elif i - 2 >= 0:
			tmp_left += max(0, current_index - x[0] - tmp_left) // 2
		elif i + 1 < n:
			tmp_left += max(0, x[-1] - tmp_left - current_index) // 2
		result = min(result, tmp_left)

		# right
		tmp_right += (x[i + 1] - x[i]) // 2
		current_index = (x[i + 1] + x[i]) // 2
		if i - 1 >= 0 and i + 2 < n:
			tmp_right += max(max(0, current_index - (x[0] + tmp_right)), max(0, x[-1] - tmp_right - current_index)) // 2
		elif i - 1 >= 0:
			tmp_right += max(0, current_index - (x[0] + tmp_right)) // 2
		elif i + 2 < n:
			tmp_right += max(0, x[-1] - tmp_right - current_index) // 2
		result = min(result, tmp_right)

		print(result)


if __name__ == "__main__":
	main()
