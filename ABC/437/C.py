def solve():
	n = int(input())
	wp = [[int(i) for i in input().split()] for _ in range(n)]

	sum_w = sum(i[0] for i in wp)
	diff = sorted((i[0] + i[1] for i in wp), reverse=True)

	for i in range(n):
		sum_w -= diff[i]
		if sum_w <= 0:
			print(n - i - 1)
			break


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
