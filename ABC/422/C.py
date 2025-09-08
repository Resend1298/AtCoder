def solve():
	a, b, c = [int(i) for i in input().split()]

	if min(a, b, c) == a or min(a, b, c) == c:
		print(min(a, b, c))
		return

	# use B first
	result = b
	a -= b
	c -= b
	if a < c:
		a, c = c, a

	if a >= 2 * c:
		result += c
		print(result)
		return

	result += (a + c) // 3
	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
