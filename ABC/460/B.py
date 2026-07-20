def solve():
	x1, y1, r1, x2, y2, r2 = [int(i) for i in input().split()]

	if abs(r1 - r2) ** 2 <= (x2 - x1) ** 2 + (y2 - y1) ** 2 <= (r1 + r2) ** 2:
		print("Yes")
	else:
		print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
