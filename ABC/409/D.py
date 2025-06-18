def main():
	t = int(input())
	for _ in range(t):
		n = int(input())
		s = input()

		for i in range(n - 1):
			if s[i] <= s[i + 1]:
				continue

			for j in range(i + 2, n):
				if s[j] > s[i]:
					print(s[:i] + s[i + 1:j] + s[i] + s[j:])
					break
			else:
				print(s[:i] + s[i + 1:] + s[i])

			break
		else:
			print(s)


if __name__ == "__main__":
	main()
