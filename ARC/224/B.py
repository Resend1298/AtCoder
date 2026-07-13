from math import isqrt


def solve():
	n = int(input())

	# Build a near-square shape: the largest possible square,
	# then one extra column along its side, then one extra row.
	# Within a strip, every tile after the first touches 2 existing tiles, so it adds 2 pairs;
	# the first tile of a strip touches only 1.

	# in the largest square, side s = isqrt(n):
	# s rows with s - 1 horizontal pairs each, plus the same vertically -> s * (s - 1) * 2
	max_square_side = isqrt(n)
	result = max_square_side * (max_square_side - 1) * 2
	n -= max_square_side ** 2

	# first tile of the extra column: touches only the square -> +1
	if n > 0:
		result += 1
		n -= 1

	# rest of the extra column, each tile touching the square and the previous tile -> +2,
	# until it completes a max_square_side * (max_square_side + 1) rectangle
	if n > 0:
		result += 2 * min(n, max_square_side - 1)
		n -= min(n, max_square_side - 1)

	# first tile of the extra row, along the rectangle's longer side: touches only the rectangle -> +1
	if n > 0:
		result += 1
		n -= 1

	# rest of the extra row, each tile touching the rectangle and the previous tile -> +2;
	# n < (max_square_side + 1) ** 2 leaves at most max_square_side - 1 tiles here, so the row never outgrows its side
	if n > 0:
		result += 2 * n

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
