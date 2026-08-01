def main():
	n = int(input())
	s = input()

	r = 0
	current = 0

	for i in range(n):
		if r > i or s[i] == 'o':
			current += 1
		r = max(r, i + 1)
		while current > 0 and r < n:
			if s[r] == 'x':
				current -= 1
			r += 1
		print(r)


if __name__ == "__main__":
	main()
