def main():
	n, m = [int(i) for i in input().split()]
	s = [[int(i) for i in list(input())] for _ in range(n)]

	score = [0] * n

	for i in range(m):
		x, y = 0, 0
		for j in s:
			match j[i]:
				case 0:
					x += 1
				case 1:
					y += 1

		if x == 0 or y == 0:
			for j in range(n):
				score[j] += 1
		elif x < y:
			for j in range(n):
				if s[j][i] == 0:
					score[j] += 1
		else:
			for j in range(n):
				if s[j][i] == 1:
					score[j] += 1

	max_score = max(score)
	result = []
	for i in range(n):
		if score[i] == max_score:
			result.append(i + 1)

	print(*result)


if __name__ == "__main__":
	main()
