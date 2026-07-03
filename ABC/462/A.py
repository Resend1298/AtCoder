def main():
	s = input()

	result = [i for i in s if i.isdigit()]

	print(''.join(result))


if __name__ == "__main__":
	main()
