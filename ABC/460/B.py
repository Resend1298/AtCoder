# TODO: review

def solve():
	x1, y1, r1, x2, y2, r2 = [int(i) for i in input().split()]

	if r1 > r2:
		x1, x2 = x2, x1
		y1, y2 = y2, y1
		r1, r2 = r2, r1

	if (x2 - x1) ** 2 + (y2 - y1) ** 2 == (r2 - r1) ** 2 or (x2 - x1) ** 2 + (y2 - y1) ** 2 == (r1 + r2) ** 2 or (
			r2 - r1) ** 2 < (x2 - x1) ** 2 + (y2 - y1) ** 2 < (r1 + r2) ** 2:
		print("Yes")
	else:
		print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
