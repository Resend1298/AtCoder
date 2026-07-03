def solve():
	a, b, x, y = [int(i) for i in input().split()]

	x, y = abs(x), abs(y)
	if a == b:
		print(a * (x + y))
		return
	if a > b:
		a, b = b, a
		x, y = y, x
	# From here on a < b is guaranteed.
	# The cheap cost `a` always lines up with horizontal moves on odd steps and vertical moves on even steps.
	# So we want to put horizontal moves on odd steps and vertical moves on even steps whenever we can.

	result = 0

	# First, pair the moves up: one horizontal then one vertical, as many pairs as possible.
	# Each such pair lands both moves on their `a`-priced step, costing 2*a.
	min_xy = min(x, y)
	result += 2 * a * min_xy
	x -= min_xy
	y -= min_xy

	# If both axes are fully consumed by the pairing, that pairing is optimal.
	if x == 0 and y == 0:
		print(result)
		return

	if x > 0:
		# Only horizontal moves are left. Consume them two at a time.
		# For each pair of horizontal moves we can either:
		#   - walk them back to back, so one falls on an even step: cost a + b, or
		#   - interleave two throwaway vertical moves (there and back):
		#     horizontal -> vertical -> horizontal -> vertical(back), cost a * 4.
		# Take whichever is cheaper.
		remaining_pair_count = x // 2
		if a + b > a * 4:
			result += a * 4 * remaining_pair_count
		else:
			result += (a + b) * remaining_pair_count
		x -= remaining_pair_count * 2

		if x == 1:
			# A single horizontal move is left, and the next step is odd,
			# so it takes it at the cheaper price `a` directly.
			result += a
	else:
		# Only vertical moves are left. Consume them two at a time.
		# For each pair of vertical moves we can either:
		#   - walk them back to back, so one falls on an odd step: cost a + b, or
		#   - interleave two throwaway horizontal moves (there and back):
		#     horizontal -> vertical -> horizontal(back) -> vertical, cost a * 4.
		# Take whichever is cheaper.
		remaining_pair_count = y // 2
		if a + b > a * 4:
			result += a * 4 * remaining_pair_count
		else:
			result += (a + b) * remaining_pair_count
		y -= remaining_pair_count * 2

		if y == 1:
			# A single vertical move is left, and the next step is odd (where vertical costs b).
			# We can either:
			#   - take it directly for cost b, or
			#   - detour: horizontal -> vertical -> horizontal(back), cost a * 3.
			result += min(b, a * 3)

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()
