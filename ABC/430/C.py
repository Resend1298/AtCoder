from sortedcontainers import SortedList


def main():
	n, a, b = [int(i) for i in input().split()]
	s = input()

	result = 0
	current_a_count = 1 if s[0] == 'a' else 0
	current_b_count = 1 if s[0] == 'b' else 0
	b_location = SortedList(i for i in range(n) if s[i] == 'b')
	r = 0

	for l in range(n):
		while r + 1 < n and current_a_count < a:
			r += 1
			if s[r] == 'a':
				current_a_count += 1
			else:
				current_b_count += 1
		if r == n - 1 and current_a_count < a:
			break

		if current_b_count < b:
			leftest_b_index = b_location.bisect_left(l)
			if leftest_b_index != len(b_location):
				right_bound_b_index = leftest_b_index + b - 1
				right_bound_b = b_location[right_bound_b_index] if right_bound_b_index < len(b_location) else n
				result += right_bound_b - r
			else:
				result += n - r

		if s[l] == 'a':
			current_a_count -= 1
		else:
			current_b_count -= 1

		if l == r and r + 1 < n:
			r += 1
			if s[r] == 'a':
				current_a_count += 1
			else:
				current_b_count += 1

	print(result)


if __name__ == "__main__":
	main()
