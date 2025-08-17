def main():
	n, m = [int(i) for i in input().split()]
	s = input()
	t = input()

	swap = [False] * n
	for _ in range(m):
		l, r = [int(i) - 1 for i in input().split()]
		swap[l] = not swap[l]
		if r + 1 < n:
			swap[r + 1] = not swap[r + 1]

	result = []
	current_swap = False
	for i in range(n):
		if swap[i]:
			current_swap = not current_swap
		result.append(s[i] if not current_swap else t[i])

	print(''.join(result))


if __name__ == "__main__":
	main()
