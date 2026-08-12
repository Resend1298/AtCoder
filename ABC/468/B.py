def main():
	m, d = [int(i) for i in input().split()]
	s = input()

	watched = [False] * m

	for i in range(m):
		if s[i] == 'G':
			for j in range(max(0, i - d), min(m, i + d + 1)):
				watched[j] = True

	print(watched.count(False))


if __name__ == "__main__":
	main()
