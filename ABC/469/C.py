def main():
	n = int(input())
	s = input()

	r = 0  # [0, r) can be eaten
	current_hit = 0

	for i in range(n):
		if r > i and s[i] == 'o':
			# discarded 1, got 1 -> got 1 = +1
			current_hit += 1
		elif r > i and s[i] == 'x':
			# discarded 1 -> None = +1
			current_hit += 1
		elif i >= r and s[i] == 'o':
			# None -> got 1 = +1
			current_hit += 1
		elif i >= r and s[i] == 'x':
			# None -> None = 0
			pass

		r = max(r, i + 1)

		while current_hit > 0 and r + 1 <= n:
			if s[r] == 'x':
				current_hit -= 1
			r += 1

		print(r)


if __name__ == "__main__":
	main()
