def main():
	l, r, d, u = [int(i) for i in input().split()]

	result = 0

	for y in range(d, u + 1):
		if y % 2 == 0:
			if l <= -abs(y) <= abs(y) <= r:
				result += abs(y) * 2 + 1
			elif l <= abs(y) <= r:
				result += abs(y) - l + 1
			elif l <= -abs(y) <= r:
				result += r - (-abs(y)) + 1
			elif -abs(y) <= l <= r <= abs(y):
				result += r - l + 1

		if y % 2 == 1:
			y = abs(y) - 1
		else:
			y = abs(y)
		if r >= y + 2:
			if l <= y + 2:
				result += (r - (y + 2)) // 2 + 1
			else:
				if l % 2 == 0:
					result += (r - l) // 2 + 1
				else:
					result += (r - (l + 1)) // 2 + 1
		if l <= -y - 2:
			if r >= -y - 2:
				result += (-y - 2 - l) // 2 + 1
			else:
				if r % 2 == 0:
					result += (r - l) // 2 + 1
				else:
					result += (r - 1 - l) // 2 + 1

	print(result)


if __name__ == "__main__":
	main()
