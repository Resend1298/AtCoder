def solve():
	n, h = [int(i) for i in input().split()]
	targets = [[int(i) for i in input().split()] for _ in range(n)]

	current_low = h
	current_high = h
	current_time = 0

	for t, target_low, target_high in targets:
		time_diff = t - current_time
		possible_low = current_low - time_diff
		possible_high = current_high + time_diff

		if possible_high < target_low or possible_low > target_high:
			print("No")
			return

		current_low = max(possible_low, target_low)
		current_high = min(possible_high, target_high)
		current_time = t

	print("Yes")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
