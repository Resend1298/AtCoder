def main():
	s = input()

	center = (len(s) + 1) // 2 - 1
	print(s[:center] + s[center + 1:])


if __name__ == "__main__":
	main()
