def main():
	n = int(input())
	s = input()

	a_index = [i for i in range(n * 2) if s[i] == 'A']

	# how many operations required to get A_A_A_...
	result_1 = 0
	for i in range(n):
		result_1 += abs(a_index[i] - i * 2)

	# how many operations required to get _A_A_A...
	result_2 = 0
	for i in range(n):
		result_2 += abs(a_index[i] - (i * 2 + 1))

	print(min(result_1, result_2))


if __name__ == "__main__":
	main()
