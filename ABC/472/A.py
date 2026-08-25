def main():
	s = input()

	result = [i if i == 'A' else '.' for i in s]

	print(''.join(result))


if __name__ == "__main__":
	main()
