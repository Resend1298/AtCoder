def main():
	n = int(input())

	next_power = 1
	good_ints = [set() for _ in range(11)]

	for digit_len in range(1, 11):
		while len(str(next_power)) == digit_len:
			good_ints[digit_len].add(next_power)
			next_power *= 2

		for l_len in range(1, digit_len):
			r_len = digit_len - l_len
			for i in good_ints[l_len]:
				for j in good_ints[r_len]:
					good_ints[digit_len].add(int(str(i) + str(j)))

		if len(good_ints[digit_len]) >= n:
			print(sorted(good_ints[digit_len])[n - 1])
			exit()

		n -= len(good_ints[digit_len])


if __name__ == "__main__":
	main()
