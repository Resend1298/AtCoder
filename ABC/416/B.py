def main():
	s = input()

	if s == '#' * len(s):
		print(s)
		exit()
	if '#' not in s:
		print('o' + '.' * (len(s) - 1))
		exit()

	result = list(s)

	o = False
	for i in range(len(s)):
		if s[i] == '#':
			o = True
		elif o and s[i] == '.':
			result[i] = 'o'
			o = False

	first = s.index('#')
	for i in range(first):
		if result[i] == '.':
			result[i] = 'o'
			break
	print(''.join(result))


if __name__ == "__main__":
	main()
