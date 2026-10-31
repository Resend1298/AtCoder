def main():
	s = [input() for _ in range(5)]

	result = float("inf")

	for i in s:
		result = min(result, 5 - i.count('o'))
	for i in zip(*s):
		result = min(result, 5 - i.count('o'))
	for i in [(s[0][0], s[1][1], s[2][2], s[3][3], s[4][4]), (s[0][4], s[1][3], s[2][2], s[3][1], s[4][0])]:
		result = min(result, 5 - i.count('o'))

	print(result)


if __name__ == "__main__":
	main()
