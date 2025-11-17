def main():
	numbers = [int(i) for i in list(input())]

	numbers.sort()

	if 0 not in numbers:
		print(''.join(str(i) for i in numbers))
	else:
		for i in numbers:
			if i != 0:
				first_digit = i
				numbers.remove(i)
				break
		# noinspection PyUnboundLocalVariable
		print(str(first_digit) + ''.join(str(i) for i in numbers))


if __name__ == "__main__":
	main()
