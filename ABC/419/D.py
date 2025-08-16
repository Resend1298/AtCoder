def main():
	n, m = [int(i) for i in input().split()]
	s = input()
	t = input()

	reverse = [False] * n

	for _ in range(m):
		l, r = [int(i) - 1 for i in input().split()]
		reverse[l] = not reverse[l]
		if r + 1 < n:
			reverse[r + 1] = not reverse[r + 1]

	result = []
	current = False
	for i in range(n):
		if reverse[i]:
			current = not current
		if not current:
			result.append(s[i])
		else:
			result.append(t[i])

	print(''.join(result))


if __name__ == "__main__":
	main()
