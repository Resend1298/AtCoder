from math import sqrt


def solve():
	n = int(input())

	square_edge_len = int(sqrt(n))
	while square_edge_len ** 2 > n:
		square_edge_len -= 1

	result = (square_edge_len - 1) * square_edge_len * 2
	remaining = n - square_edge_len * square_edge_len

	if remaining == 0:
		print(result)
		return

	result += 1
	remaining -= 1
	if remaining == 0:
		print(result)
		return

	next_part = min(remaining, square_edge_len - 1)
	result += 2 * next_part
	remaining -= next_part
	if remaining == 0:
		print(result)
		return

	result += 1
	remaining -= 1
	if remaining == 0:
		print(result)
		return

	result += 2 * remaining
	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
