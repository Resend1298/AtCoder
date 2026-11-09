# TODO: review

def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	current_max = 0
	current_min = 0
	current = 0
	for i in a:
		current += i
		current_max = max(current_max, current)
		current_min = min(current_min, current)
	result = current_max - current_min + 1

	dp = []
	current_min = 0
	current_max = 0
	current = 0
	for i in range(n):
		tmp_current = current - a[i]
		tmp_current_min = min(current_min, tmp_current)
		tmp_current_max = max(current_max, tmp_current)
		dp.append((tmp_current_min, tmp_current_max, tmp_current, i))

		current += a[i]
		current_max = max(current_max, current)
		current_min = min(current_min, current)

	tmp_current_min, tmp_current_max, tmp_current, i = dp.pop()
	result = max(result, tmp_current_max - tmp_current_min + 1)

	current = 0
	current_min = 0
	current_max = 0

	for tmp_current_min, tmp_current_max, tmp_current, i in dp[::-1]:
		if i == n - 2:
			if a[i + 1] > 0:
				current_min = -a[i + 1]
				current_max = 0
			else:
				current_min = 0
				current_max = -a[i + 1]
		current_min += a[i + 1]
		current_max += a[i + 1]
		current_min = min(current_min, 0)
		current_max = max(current_max, 0)

		tmp_current_min = min(tmp_current_min, tmp_current + current_min)
		tmp_current_max = max(tmp_current_max, tmp_current + current_max)
		result = max(result, tmp_current_max - tmp_current_min + 1)

	print(result)


if __name__ == "__main__":
	main()
