def main():
	n = int(input())
	s = input()

	for i in range(n):
		if s[i] != 'o':
			print(s[i:])
			break


if __name__ == "__main__":
	main()
