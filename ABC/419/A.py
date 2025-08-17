def main():
	s = input()
	atcoder = {"red": "SSS", "blue": "FFF", "green": "MMM"}

	if s in atcoder:
		print(atcoder[s])
	else:
		print("Unknown")


if __name__ == "__main__":
	main()
