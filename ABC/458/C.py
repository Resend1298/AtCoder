def main():
	s = input()

	c_index = [i for i in range(len(s)) if s[i] == 'C']
	result = 0

	for i in c_index:
		result += min(i, len(s) - i - 1) + 1

	print(result)


if __name__ == "__main__":
	main()
