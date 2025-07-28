def main():
	s = input()

	t = list(s)
	changeable = True

	for i in range(len(s)):
		if s[i] == '#':
			changeable = True
		elif s[i] == '.' and changeable:
			t[i] = 'o'
			changeable = False

	print(''.join(t))


if __name__ == "__main__":
	main()
