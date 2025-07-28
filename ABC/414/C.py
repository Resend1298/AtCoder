# CPython TLE, PyPy AC

def base_convert(n: int, base) -> str:
	result = []
	while n != 0:
		result.append(str(n % base))
		n //= base
	result.reverse()
	return ''.join(result)


def palindromic_in_base(n: int, base) -> bool:
	n_base = base_convert(n, base)
	return n_base == n_base[::-1]


def main():
	a = int(input())
	n = int(input())

	result = 0

	for i in range(1, min(n, 9) + 1):
		if palindromic_in_base(i, a):
			result += i

	for number_of_digits in range(2, len(str(n)) + 1):
		match number_of_digits % 2:
			case 0:
				for palindromic_part in range(10 ** (number_of_digits // 2 - 1), 10 ** (number_of_digits // 2)):
					current = int(str(palindromic_part) + str(palindromic_part)[::-1])
					if current > n:
						break
					if palindromic_in_base(current, a):
						result += current
			case 1:
				for palindromic_part in range(10 ** (number_of_digits // 2 - 1), 10 ** (number_of_digits // 2)):
					for middle_digit in range(10):
						current = int(str(palindromic_part) + str(middle_digit) + str(palindromic_part)[::-1])
						if current > n:
							break
						if palindromic_in_base(current, a):
							result += current

	print(result)


if __name__ == "__main__":
	main()
