def solve():
	n = int(input())
	reindeers = [[int(i) for i in input().split()] for _ in range(n)]

	diff = [i[0] + i[1] for i in reindeers]
	diff.sort()
	current_diff = sum(i[0] for i in reindeers)
	result = n

	while current_diff > 0:
		result -= 1
		current_diff -= diff.pop()

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
