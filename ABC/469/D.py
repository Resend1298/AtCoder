def main():
	n, m = [int(i) for i in input().split()]
	ab = [[int(i) - 1 for i in input().split()] for _ in range(m)]

	x = ab[0][0]
	y = ab[0][1]
	possible_x = set()
	possible_y = set()
	x_possible = True
	y_possible = True

	for a, b in ab[1:]:
		if x_possible:
			if x != a and x != b:
				if not possible_x:
					possible_x.add(a)
					possible_x.add(b)
				else:
					if a not in possible_x and b not in possible_x:
						x_possible = False
					else:
						possible_x &= {a, b}

		if y_possible:
			if y != a and y != b:
				if not possible_y:
					possible_y.add(a)
					possible_y.add(b)
				else:
					if a not in possible_y and b not in possible_y:
						y_possible = False
					else:
						possible_y &= {a, b}

	result = 0
	if x_possible:
		if not possible_x:
			result += n - 1
		else:
			result += len(possible_x)
	if y_possible:
		if not possible_y:
			result += n - 1
		else:
			result += len(possible_y)

	if x_possible and y_possible:
		if (not possible_x) or (not possible_y):
			result -= 1
		elif y in possible_x and x in possible_y:
			result -= 1

	print(result)


if __name__ == "__main__":
	main()
