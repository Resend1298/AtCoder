def solve():
	n, h = [int(i) for i in input().split()]
	tlu = [[int(i) for i in input().split()] for _ in range(n)]

	current_t = 0
	possible_high = h
	possible_low = h

	for t, l, u in tlu:
		if possible_high + t - current_t < l or possible_low - (t - current_t) > u:
			print("No")
			break

		possible_high = min(possible_high + t - current_t, u)
		possible_low = max(possible_low - (t - current_t), l)
		current_t = t
	else:
		print("Yes")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
