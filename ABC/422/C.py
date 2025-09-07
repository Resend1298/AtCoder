def solve():
	a, b, c = [int(i) for i in input().split()]

	if min(a, b, c) == a or min(a, b, c) == c:
		print(min(a, b, c))
		return

	result = b
	a -= b
	c -= b
	b = 0

	if c > a:
		a, c = c, a

	if a - c >= c:
		result += c
		print(result)
		return

	result += a - c
	tmp = a - c
	a -= 2 * tmp
	c -= tmp
	result += (a + c) // 3
	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
