def main():
	n, m = [int(i) for i in input().split()]
	ab = [[int(i) - 1 for i in input().split()] for _ in range(m)]

	# possible pairs must be in the form of (a0, x) or (b0, x)
	a0, b0 = ab[0]
	a0_x = set(range(n))
	a0_x.remove(a0)
	b0_x = set(range(n))
	b0_x.remove(b0)

	for a, b in ab[1:]:
		if a0 not in (a, b):
			a0_x &= {a, b}
		if b0 not in (a, b):
			b0_x &= {a, b}

	result = len(a0_x) + len(b0_x)
	if b0 in a0_x:
		result -= 1
	print(result)


if __name__ == "__main__":
	main()
