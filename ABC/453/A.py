def main():
	n = int(input())
	s = input()

	result = []

	for i in range(n):
		if s[i] != 'o':
			for j in range(i, n):
				result.append(s[j])
			break

	print(''.join(result))


if __name__ == "__main__":
	main()
