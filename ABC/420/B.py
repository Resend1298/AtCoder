def main():
	n, m = [int(i) for i in input().split()]
	s = [[int(i) for i in list(input())] for _ in range(n)]

	point = [0] * n

	for i in range(m):
		x, y = 0, 0
		for j in range(n):
			if s[j][i] == 0:
				x += 1
			else:
				y += 1

		if x == 0 or y == 0:
			for j in range(n):
				point[j] += 1
		elif x < y:
			for j in range(n):
				if s[j][i] == 0:
					point[j] += 1
		else:
			for j in range(n):
				if s[j][i] == 1:
					point[j] += 1

	max_point = max(point)
	result = []
	for i in range(n):
		if point[i] == max_point:
			result.append(i + 1)

	print(*result)


if __name__ == "__main__":
	main()
