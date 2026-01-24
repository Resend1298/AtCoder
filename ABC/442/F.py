def main():
	n = int(input())
	s = [input() for _ in range(n)]

	current = s[0].count('.')
	tmp = [current]
	for i in s[0]:
		if i == '.':
			current -= 1
		else:
			current += 1
		tmp.append(current)
	min_tmp = [0] * (n + 1)
	min_tmp[-1] = tmp[-1]
	for i in range(n - 1, -1, -1):
		min_tmp[i] = min(min_tmp[i + 1], tmp[i])

	for i in range(1, n):
		current = s[i].count('.')
		new_tmp = [current + min_tmp[0]]
		for j in range(n):
			if s[i][j] == '.':
				current -= 1
			else:
				current += 1
			new_tmp.append(current + min_tmp[j + 1])
		min_tmp[-1] = new_tmp[-1]
		for j in range(n - 1, -1, -1):
			min_tmp[j] = min(min_tmp[j + 1], new_tmp[j])

	print(min_tmp[0])


if __name__ == "__main__":
	main()
