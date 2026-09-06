from collections import deque


def solve():
	n = int(input())
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	coupon = float("inf")
	for i in range(n):
		coupon = min(coupon, ab[i][0])

	ab.sort(key=lambda x: x[0] - x[1])
	ab = deque(ab)

	result = 0
	while len(ab) >= 2 and ab[0][0] + ab[-1][1] <= ab[0][1] + ab[-1][1] + coupon * 2:
		result += ab[0][0]
		result += ab[-1][1]
		ab.popleft()
		ab.pop()

	for a, b in ab:
		result += min(a, b + coupon)

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
