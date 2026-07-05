def solve():
	x, y, k = [int(i) for i in input().split()]

	result = 0
	while x != y:
		result += 1
		if x > y:
			x //= k
		else:
			y //= k

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
