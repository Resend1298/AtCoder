def main():
	s = input()

	location = []
	for i in range(len(s)):
		if s[i] == '#':
			location.append(i)

	for i in range(0, len(location) - 1, 2):
		print(f"{location[i] + 1},{location[i + 1] + 1}")


if __name__ == "__main__":
	main()
