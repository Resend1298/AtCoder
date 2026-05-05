def main():
	s = input()

	possibilities_end_with = {'a': 0, 'b': 0, 'c': 0}
	for i in s:
		possibilities_end_with[i] = sum(possibilities_end_with.values()) + 1
		possibilities_end_with[i] %= 998244353

	print(sum(possibilities_end_with.values()) % 998244353)


if __name__ == "__main__":
	main()
